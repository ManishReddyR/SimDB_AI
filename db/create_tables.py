""" This script initializes the database by creating tables defined in the schema."""

# Import necessary libraries 
from db.schema import Base
from db.connection import engine

# Function to initialize the database by creating tables
def init_db():
    Base.metadata.create_all(bind=engine)
    print(" Tables created.")   