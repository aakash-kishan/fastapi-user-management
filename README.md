# FastAPI User Management API

A simple User Management API built using:

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (can be switched to PostgreSQL)

## Features

- Create User
- Update User
- Get Single User
- List Users
  - Pagination
  - Filtering
  - Sorting
  - Search by Name/Email
- Bulk Create Users

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

## Project Structure

```text
app/
├── database.py
├── dependencies.py
├── models.py
├── schemas.py
├── crud.py
├── main.py
└── routes/
    └── users.py
```