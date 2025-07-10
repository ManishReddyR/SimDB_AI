# SimDB AI

## Project Overview

This project builds a system to define, interpret, and execute symbolic/mathematical models (ODEs, PDEs) described in natural language or JSON. The system uses AI agents (based on LangChain and OpenAI) to interact with a PostgreSQL database for storing model specifications and experiments. It enables:

- Defining models using JSON or natural language.
- AI-driven insertion and retrieval of models.
- Database-backed experiment tracking.
- Integration with Model Context Protocol (MCP) for standardized AI responses.
- Interactive command-line interface to query and update models.

## Features

- **Model Storage:** Store and retrieve symbolic model specifications with parameters and initial conditions.
- **AI Agent Integration:** Use OpenAI-powered LangChain agents to interpret natural language queries and manage the database.
- **Experiment Tracking:** Support for experiments tied to models (future extension).
- **MCP Integration:** Responses wrapped with metadata for consistent interpretation.
- **Database Management:** Automatic creation of PostgreSQL database and tables.
- **CLI Interface:** Interactive terminal to query or insert models via natural language or JSON.

## Architecture

- Backend: Python, SQLAlchemy, PostgreSQL
- AI: OpenAI GPT models accessed via LangChain
- Embeddings & Metadata: MCP protocol for wrapping results
- CLI Interface for user interaction

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL installed and running
- An OpenAI API key
- `DATABASE_URL` environment variable set (e.g. `postgresql+psycopg2://user:password@localhost:5432/modeldb`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ManishReddyR/SimDB_AI.git
cd SimDB_AI
```

2. Create and activate a Python virtual enviornment:
``` bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requriements.txt
```

4. Setup .env file:
```ini
OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
DATABASE_URL='YOUR_DATABASE_URL'
DB_USER='YOUR_DB_USERNAME'
DB_PASS='YOUR_DB_PASSWORD'
DB_HOST='YOUR_DB_HOST'
DB_PORT='YOUR_DB_PORT'
```

### Usage

Run the main pogram:
```bash
python3 main.py
```

You will see the prompt
```bash
>>
```

Type natural language queries or JSON model definitions, for example:
```bash
Insert or retrieve this model: {"name": "Simple Pendulum", "description": "Undamped pendulum system", "equations": "d2theta/dt2 + (g/l) * sin(theta) = 0", "params": {"g": 9.8, "l": 1.0}, "initial_conditions": {"theta": 0.5, "dtheta": 0.0}}
```

Type exit or quit to close program.

### Project Structure:

```
SimDB_AI/
├── agent/
│   └── langchain_agent.py          # LangChain agent setup and initialization
│   ├── tools.py                    # Tool functions for database operations (used by the agent)
├── db/
│   ├── connection.py               # SQLAlchemy database connection setup
│   ├── create_database.py          # Create the database if it doesn't exist
│   ├── create_tables.py            # Create tables using SQLAlchemy metadata
│   └── schema.py                   #  SQLAlchemy ORM models (Model, Experiment)
├── mcp/
│   └── protocol.py                 # Wrap responses in MCP-compliant format
├── .env                            # Environment variables (e.g., DATABASE_URL)
├── main.py                         # Main CLI entry point for the agent interface
├── requirements.txt                # Python package dependencies
└── README.md                       # Project documentation
```
