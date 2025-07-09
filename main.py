""" This is the main entry point for the SimDB AI application. It initializes the database and starts an interactive agent session. """

# Import nessary libraries
from db.create_database import create_database_if_not_exists
from db.create_tables import init_db
from agent.langchain_agent import get_agent

if __name__ == "__main__":
    # Ensure DB and tables are ready
    create_database_if_not_exists()
    init_db()

    # Start interactive agent session
    agent = get_agent()

    while True:
        query = input("\n>> ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Exiting. Goodbye!")
            break

        try:
            response = agent.run(query)
            print("\n📦 Response:\n", response)
        except Exception as e:
            print("❌ Error:", e)
