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

# Schema for returning a Post response with owner's email
class PostOwner(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True

# Schema for returning a Post response
class PostResponse(PostBase):
    id: int  # ID of the post
    created_at: datetime  # Timestamp when the post was created
    owner: PostOwner  # Owner info (id and email)

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

class Token(BaseModel):
    access_token: str  # Access token for authentication
    token_type: str  # Type of the token (e.g., "bearer")
class TokenData(BaseModel):
    id: Optional[int] = None  # ID of the user associated with the token, optional
    email: Optional[EmailStr] = None  # Email of the user associated with the token, optional