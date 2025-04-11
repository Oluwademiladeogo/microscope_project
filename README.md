# Microscope Project

This document provides instructions on how to set up and run the Microscope Project locally.

## Setup

1.  **Unzip the project archive:**
    If you have downloaded the project as a zip file, extract it first.
    ```bash
    unzip microscope_project.zip # Or the name of your zip file
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd microscope_project
    ```

3.  **Install dependencies:**
    This command installs all the required Python packages listed in the `requirements.txt` file. Make sure you have a virtual environment activated.
    ```bash
    python -m pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    This command sets up or updates the database schema based on the project's models.
    ```bash
    python manage.py migrate
    ```

## Running the Development Server

To run the application using Gunicorn with Uvicorn workers:

```bash
python -m gunicorn microscope_project.asgi:application -k uvicorn.workers.UvicornWorker