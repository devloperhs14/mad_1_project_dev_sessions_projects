# Homework 1

A Python project, likely using the Flask framework.

## Description

*(Please add a brief description of your project here.)*

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/devloperhs14/mad_1_project_dev_sessions_projects.git
    cd user_input_display
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *(Note: It seems a virtual environment might already exist at `homework1\homework1`. You might want to use that or create a new one as shown above.)*

3.  **Install dependencies:**
    *(Assuming you have a `requirements.txt` file)*
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt`, you can create one using `pip freeze > requirements.txt` after installing necessary packages.)*

## Running the Application

```bash
# Make sure your terminal is in the project's root directory
# and the virtual environment is activated.

# Set the Flask application entry point (if not app.py or wsgi.py)
# export FLASK_APP=your_app_file.py  (macOS/Linux)
# set FLASK_APP=your_app_file.py    (Windows)

flask run
```
Or, if you have a main script:
```bash
python app.py
```