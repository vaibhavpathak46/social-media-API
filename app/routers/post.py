from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from .. import oauth2

# Initialize the router with a prefix and tags for better organization
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# Route to create a new post (protected)
@router.post("/", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    """Create a new post and save it to the database. Only the authenticated user can create their own post."""
    new_post = models.Post(**post.dict(), owner_id=get_current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Route to get all posts (protected)
@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), get_current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    """Retrieve all posts from the database, including owner's email."""
    posts = db.query(models.Post).all()
    return posts

# Route to get a single post by ID (protected)
@router.get("/{post_id}", response_model=schemas.PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db), get_current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    """Retrieve a single post by its ID, including owner's email."""
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

# Route to update a post (protected)
@router.put("/{post_id}", response_model=schemas.PostResponse)
def update_post(post_id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    """Update an existing post by its ID. Only the owner can update their post."""
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this post")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

# Route to delete a post (protected)
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), get_current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    """Delete a post by its ID. Only the owner can delete their post."""
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
    post_query.delete(synchronize_session=False)
    db.commit()
    return
