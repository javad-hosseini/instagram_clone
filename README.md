# Instagram Clone

A learning project built with **FastAPI**, **React**, and **REST Architecture** to understand how modern full-stack web applications work.

The goal of this project was not to create a production-ready social media platform, but to gain hands-on experience with backend development, frontend integration, authentication, database modeling, and client-server communication.

---

## Project Overview

This project is a simplified Instagram-inspired application that allows users to authenticate, create posts, upload images, and interact with content through a REST API.

The backend is built using FastAPI and follows REST principles, while the frontend is developed with React.

---

## Features

* User Registration
* User Login
* JWT Authentication
* Create Posts
* View Posts Feed
* Upload and Display Images
* Add Comments to Posts
* View Comments
* RESTful API Architecture
* React Frontend Integration
* SQLite Database Storage

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication
* Python

### Frontend

* React
* Bootstrap
* CSS

---

## Authentication

Authentication is implemented using **JWT (JSON Web Tokens)**.

After a successful login:

1. The server generates an access token.
2. The token contains user information and an expiration time.
3. Protected routes require a valid Bearer token.
4. User identity is verified on every authenticated request.

Current token expiration time:

* 30 minutes

Algorithm used:

* HS256

---

## Project Structure

```text
instagram_clone/
│
├── auth/
├── db/
├── routers/
├── images/
├── instagram-clone-UI/
│
├── main.py
├── requirements.txt
├── ig_api.db
└── run-project.bat
```

---

## What I Learned

This project helped me gain practical experience in:

* Building REST APIs with FastAPI
* Database Modeling with SQLAlchemy
* JWT Authentication
* Client-Server Communication
* React State Management
* Frontend and Backend Integration
* API Design Principles
* Debugging Full-Stack Applications
* Working with Relational Databases

---

## Running the Project

### Backend

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

---

### Frontend

Navigate to the React application:

```bash
cd instagram-clone-UI
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

---

## Future Improvements

Some features that could be added in future versions:

* Like System
* User Profiles
* Follow / Unfollow Users
* Dark Mode
* Search Functionality
* Notifications
* Better Responsive Design
* Image Optimization
* PostgreSQL Support
* Docker Deployment

---

## Educational Purpose

This project was created as a learning exercise while studying FastAPI, React, REST APIs, authentication, and full-stack application development.

The main focus was understanding concepts, architecture, and communication between frontend and backend systems rather than building a production-ready clone.

---

## Author

**Javad Hosseini**

Computer Engineering Student

GitHub:
https://github.com/javad-hosseini
