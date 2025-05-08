# Todo App with FastAPI

This is a simple Todo application built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## Features

- Create, read, update, and delete (CRUD) todos.
- RESTful API endpoints.
- Lightweight and easy to use.
- Built-in validation using Pydantic.
- Asynchronous support for better performance.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/todo-app-fastapi.git
    cd todo-app-fastapi
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the development server:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000`.

3. Access the interactive API documentation at `http://127.0.0.1:8000/docs` (Swagger UI) or `http://127.0.0.1:8000/redoc`.

## Project Structure

```
todo-app-fastapi/
│
├── main.py             # Entry point of the application
├── models.py           # Pydantic models for data validation
├── routes.py           # API route definitions
├── database.py         # Database setup and operations
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## API Endpoints

- `GET /todos` - Retrieve all todos.
- `GET /todos/{id}` - Retrieve a specific todo by ID.
- `POST /todos` - Create a new todo.
- `PUT /todos/{id}` - Update an existing todo by ID.
- `DELETE /todos/{id}` - Delete a todo by ID.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

Feel free to contribute to this project by submitting issues or pull requests!