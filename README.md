# Flask Application with RESTful API

This project is a simple Flask web application that demonstrates basic web routing and a RESTful API for managing users. It covers HTTP verbs (GET, POST, PUT, DELETE) and working with JSON data.

## Overview

- The main web app (`app.py`) provides basic routes for web pages.
- The API (`api.py`) allows you to create, read, update, and delete users using JSON data.

## Files

- `app.py`: Main application file with basic web routes.
- `api.py`: RESTful API for user management (CRUD operations).
- `requirements.txt`: Lists Python dependencies.
- `README.md`: Project documentation.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/flask.git
   cd flask
   ```

2. **Create a virtual environment (recommended):**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

### Run the Web Application

```
python app.py
```
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### Run the API

```
python api.py
```
You can interact with the API using tools like [Postman](https://www.postman.com/) or `curl`.

#### API Endpoints

- `GET /api/users` — List all users
- `GET /api/users/<id>` — Get a user by ID
- `POST /api/users` — Create a new user (JSON: `{ "name": "YourName" }`)
- `PUT /api/users/<id>` — Update a user's name (JSON: `{ "name": "NewName" }`)
- `DELETE /api/users/<id>` — Delete a user

#### Example `curl` Commands

- **Get all users:**
  ```
  curl http://127.0.0.1:5000/api/users
  ```
- **Add a user:**
  ```
  curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Charlie\"}" http://127.0.0.1:5000/api/users
  ```
- **Update a user:**
  ```
  curl -X PUT -H "Content-Type: application/json" -d "{\"name\": \"Alice Updated\"}" http://127.0.0.1:5000/api/users/1
  ```
- **Delete a user:**
  ```
  curl -X DELETE http://127.0.0.1:5000/api/users/1
  ```

## License

This project is for educational purposes.
