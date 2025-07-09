"""Script to define the database schema using SQLAlchemy"""

# Import necessary libraries and modules
from sqlalchemy import Column, Integer, Text, JSON, ForeignKey, TIMESTAMP, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# Define the base class for declarative models
Base = declarative_base()

# Define the Model class representing the 'models' table
class Model(Base):
    __tablename__ = 'models'  # Table name in the database
    model_id = Column(Integer, primary_key=True)
    name = Column(Text) 
    description = Column(Text)
    spec = Column(JSON)
    code_path = Column(Text)
    approved = Column(Boolean, default=False)
    embedding = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

# Define the Experiment class representing the 'experiments' table
class Experiment(Base):
    __tablename__ = 'experiments'  # Table name in the database
    experiment_id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('models.model_id'))

    params = Column(JSON, nullable=False)
    initial_condition = Column(JSON, nullable=False)
    result = Column(JSON, nullable=True)

    hash_id  = Column(Text, unique=True)
    vector = Column(Text, nullable=True)
    embedding = Column(Text)

    created_at = Column(TIMESTAMP, server_default=func.now())