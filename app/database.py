# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL for PostgreSQL
DATABASE_URL = "postgresql://postgres:newpassword@localhost/FastAPI"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session maker for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for defining database models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        yield db
    finally:
        # Close the database session
        db.close()