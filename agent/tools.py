""" This script defines a tool for inserting or retrieving models from a database using LangChain and SQLAlchemy."""

# Import necessary libraries
from langchain_core.tools import tool
from db.connection import SessionLocal
from db.schema import Model
from mcp.protocol import wrap_mcp_response
from sqlalchemy import select
from pydantic import BaseModel, ValidationError
import json

# Define the input model for the tool
class ModelInput(BaseModel):
    name: str
    description: str
    equations: str
    params: dict
    initial_conditions: dict

# Define the tool for inserting or retrieving models
@tool
def insert_or_retrieve_model(data: str) -> dict:
    """
    Insert or retrieve a model.
    If the model already exists, return its info with creation date.
    If it doesn't exist, insert it and return confirmation with creation date.
    Accepts input as a string containing a JSON object.
    """
    try:
        json_start = data.find('{')
        if json_start == -1:
            return wrap_mcp_response(" No JSON found in input.", "model-error", data)

        json_str = data[json_start:]
        model_dict = json.loads(json_str)
        model_input = ModelInput(**model_dict)
    except json.JSONDecodeError as e:
        return wrap_mcp_response(f" JSON decode error: {str(e)}", "model-error", data)
    except ValidationError as ve:
        return wrap_mcp_response(f" Pydantic validation error: {ve}", "model-error", data)

    session = SessionLocal()
    stmt = select(Model).where(Model.name == model_input.name)
    existing = session.execute(stmt).scalar_one_or_none()

    if existing:
        response = wrap_mcp_response(
            {
                "message": f"✅ Model '{existing.name}' already exists.",
                "model_id": existing.model_id,
                "description": existing.description,
                "created_at": str(existing.created_at),
                "spec": existing.spec
            },
            context_id="model-exists",
            query=f"Insert or retrieve model: {model_input.name}"
        )
        session.close()
        return response

    model = Model(
        name=model_input.name,
        description=model_input.description,
        spec={
            "equations": model_input.equations,
            "params": model_input.params,
            "initial_conditions": model_input.initial_conditions
        },
        code_path=None,
        approved=False
    )
    session.add(model)
    session.commit()
    session.refresh(model)  # ensure created_at is populated

    response = wrap_mcp_response(
        {
            "message": f" Model '{model.name}' inserted successfully.",
            "model_id": model.model_id,
            "description": model.description,
            "created_at": str(model.created_at),
            "spec": model.spec
        },
        context_id="model-inserted",
        query=f"Insert or retrieve model: {model_input.name}"
    )

    session.close()
    return response
