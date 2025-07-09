"""This script initializes the LangChain agent with tools for inserting or retrieving models from a database."""

# Import necessary libraries
from langchain.agents import initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import AgentType
import os
from agent.tools import insert_or_retrieve_model

# Function to get the LangChain agent
def get_agent():
    # initialize the OpenAI chat model with specific parameters
    llm = ChatOpenAI(temperature=0,
                    model="gpt-4.1-nano")

    # Tools for the agent
    tools = [insert_or_retrieve_model]

    # Initialize the agent with the tools and language model
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
