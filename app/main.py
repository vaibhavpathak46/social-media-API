# Import necessary modules from FastAPI and SQLAlchemy
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models
from .routers import post, user,auth 
from .database import engine


# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Include routers for posts and users
app.include_router(user.router)  # Include the user router  
app.include_router(post.router)  # Include the post router
app.include_router(auth.router)  # Include the auth router

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}