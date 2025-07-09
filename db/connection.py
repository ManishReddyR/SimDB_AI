""" This script sets up the database connection using SQLAlchemy."""

# Import necessary libraries
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

# Load environment variables from .env file
load_dotenv()
database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Create the SQLAlchemy engine and session
engine = create_engine(database_url)    
SessionLocal = sessionmaker(bind=engine)