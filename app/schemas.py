# Import necessary modules from Pydantic and Python standard library
from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

# Base schema for a Post
class PostBase(BaseModel):
    title: str  # Title of the post
    content: str  # Content of the post
    published: Optional[bool] = True  # Whether the post is published (default: True)

# Schema for creating a new Post
class PostCreate(PostBase):
    pass  # Inherits all fields from PostBase

# Schema for returning a Post response
class PostResponse(PostBase):
    id: int  # ID of the post
    created_at: datetime  # Timestamp when the post was created

    class Config:
        from_attributes = True  # Enable ORM mode for Pydantic models

class UserCreate(BaseModel):
    email:  EmailStr  # Email of the user
    password: str  # Password of the user
    
class UserResponse(BaseModel):
    id: int  # ID of the user
    email: EmailStr  # Email of the user
    created_at: datetime  # Timestamp when the user was created

    class Config:
        from_attributes = True  # Enable ORM mode for Pydantic models

class UserLogin(BaseModel):
    email: EmailStr  # Email of the user
    password: str  # Password of the user
  