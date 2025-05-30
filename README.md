# Flask Application

This project is a simple Flask web application that demonstrates the basic structure and functionality of a Flask app.

## Overview

The application creates an instance of the Flask class and defines a single route, `/index`, which returns a welcome message when accessed.

## Files

- `app.py`: The main application file that initializes the Flask app and defines routes.
- `requirements.txt`: A file that lists the dependencies required for the application.
- `README.md`: This documentation file.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python app.py
```

The application will start, and you can access it at `http://127.0.0.1:5000/index`. You should see the welcome message displayed on the page.