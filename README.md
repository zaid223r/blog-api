
Blog Web API
===
The Blog Web API allows users to create, read, update, and delete blog posts, as well as manage users. Powered by FastAPI and SQLAlchemy, this API provides a modern and efficient solution for managing blog content and user data.
## Table of Contents
1. [Beginners Guide](#beginners-guide)
2. [API Endpoints](#api-endpoints)
    - [Create User](#create-user)
    - [Create Post](#create-post)
    - [Get Post](#get-post)
    - [Get User](#get-user)
    - [Delete Post](#delete-post)
3. [Usage](#usage)
4. [Features](#features)
5. [File Details](#file-details)


## Beginners Guide

If you are a total beginner to this, start here!

1. Clone the repository:
    ```bash
    git clone https://github.com/zaid223r/blog-api.git
    ```
2. Navigate to the project directory:
    ```bash
    cd blog-api
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Database Setup:
Make sure you have **MySQL** installed and running on your system.
Update the database connection details in database.py with your **MySQL** database connection details.
Run the following command to create the necessary database tables:
    ```bash
    python main.py
    ```
5. Run the development server:
    ```bash
    uvicorn main:app --reload
    ```
The application should now be accessible at http://localhost:8000.

## API Endpoints

### Create User

- **URL**: `/users/`
- **Method**: `POST`
- **Description**: Create a new user.

### Create Post

- **URL**: `/posts/`
- **Method**: `POST`
- **Description**: Create a new blog post.

### Get Post

- **URL**: `/posts/{post_id}/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific blog post by ID.

### Get User

- **URL**: `/users/{user_id}/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific user by ID.

### Delete Post

- **URL**: `/posts/{post_id}/`
- **Method**: `DELETE`
- **Description**: Delete a specific blog post by ID.


Usage
---
To start using the API, you can explore the available endpoints using **Swagger UI**. Simply navigate to http://localhost:8000/docs in your web browser to access the interactive API documentation.

Features
---
* **CRUD Operations:** Perform CRUD (Create, Read, Update, Delete) operations on blog posts and users.
* **Customizable Endpoints:** Extend and customize endpoints as needed to suit your application requirements.
* **Validation:** Input validation using **Pydantic** models to ensure data integrity and consistency.

File Details
---
**main.py:** This file contains the main **FastAPI** application setup, including the definition of API endpoints and their respective functions. It's where the routes and business logic for handling requests are implemented.

**models.py:** This file defines the data models for the blog API using **SQLAlchemy**'s declarative base. It includes classes representing database tables, such as User and Post, along with their respective columns and relationships.

**database.py:** This file contains the database configuration and session management setup using **SQLAlchemy**. It establishes the connection to the MySQL database and provides a session factory function for interacting with the database.
