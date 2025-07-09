"""This script creates a PostgreSQL database if it does not already exist."""

# Import necessary libraries
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_NAME = "modeldb"
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Function to create the database if it does not exist
def create_database_if_not_exists():
    conn = psycopg2.connect(
        dbname="postgres", user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (DB_NAME,))
    exists = cur.fetchone()

    if not exists:
        cur.execute(f"CREATE DATABASE {DB_NAME}")
        print(f" Created database '{DB_NAME}'")
    else:
        print(f" Database '{DB_NAME}' already exists")

    cur.close()
    conn.close()