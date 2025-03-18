# Task Management API

## Overview
This FastAPI-based application provides a simple task management system with functionalities to add and retrieve tasks. The API uses an asynchronous database setup with SQLAlchemy and SQLite.

## Algorithm Description
1. **Application Lifecycle Management**:
   - At startup, the database is cleared and then recreated.
   - Upon shutdown, a message is printed.

2. **Database Operations**:
   - The database is managed using SQLAlchemy with an asynchronous SQLite engine.
   - Tables are created dynamically at startup and removed on request.

3. **Repository Pattern**:
   - A repository class (`TaskRepository`) is used to interact with the database.
   - It includes methods for adding new tasks and retrieving all tasks.

4. **API Endpoints**:
   - `POST /tasks`: Adds a new task.
   - `GET /tasks`: Retrieves all tasks.

## Libraries Used

### 1. **FastAPI**
   - Provides the web framework for building the API.
   - Handles request routing and dependency injection.

### 2. **SQLAlchemy (async)**
   - Manages database interactions asynchronously.
   - Provides ORM capabilities with models and queries.

### 3. **Pydantic**
   - Used for data validation and serialization.
   - Ensures request and response schemas are properly structured.

### 4. **Contextlib (asynccontextmanager)**
   - Manages the application lifecycle by handling startup and shutdown operations.

## File Structure
- `main.py` - Initializes the FastAPI application and sets up database lifecycle management.
- `databaswe.py` - Contains database connection setup and ORM models.
- `rep.py` - Implements the repository pattern for database operations.
- `router.py` - Defines API endpoints and routes.
- `schemas.py` - Defines Pydantic models for request and response validation.

## Running the Application
To run the application, use the following command:

```sh
uvicorn main:app --reload
```

This will start the FastAPI server and enable automatic reloading during development.