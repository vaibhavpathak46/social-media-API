# Social Media API

A simple social media REST API built with FastAPI and SQLAlchemy.

## Features

- User registration and authentication (JWT-based)
- CRUD operations for posts
- User management
- Modular code structure using FastAPI routers
- SQLAlchemy ORM for database interactions

## Project Structure

```
app/
  main.py           # FastAPI app entry point
  models.py         # SQLAlchemy models
  database.py       # Database connection and session
  schemas.py        # Pydantic schemas
  oauth2.py         # OAuth2/JWT logic
  utils.py          # Utility functions
  routers/
    user.py         # User-related endpoints
    post.py         # Post-related endpoints
    auth.py         # Authentication endpoints
myvenv/             # Python virtual environment
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```cmd
   git clone https://github.com/vaibhavpathak46/social-media-API.git
   cd social-media-API
   ```

2. Create and activate a virtual environment:
   ```cmd
   python -m venv myvenv
   myvenv\Scripts\activate
   ```

3. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the FastAPI server:
   ```cmd
   uvicorn app.main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

3. API documentation is available at:
   ```
   http://127.0.0.1:8000/docs
   ```

## API Endpoints

- `POST /users/` - Register a new user
- `POST /login/` - Authenticate and get JWT token
- `GET /posts/` - List all posts
- `POST /posts/` - Create a new post
- `PUT /posts/{id}` - Update a post
- `DELETE /posts/{id}` - Delete a post


