""" This script defines a function to wrap the raw output of a PostgreSQL query into a structured response format for the MCP protocol."""

def wrap_mcp_response(raw_output: str, context_id: str, query: str) -> dict:
    return {
        "context_id": context_id,
        "source": "postgresql_query",
        "input_query": query,
        "result": raw_output
    }
