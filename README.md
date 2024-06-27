# Django Ninja Car API

A Django Ninja project for managing car information with REST API endpoints for the coding challenge from oneclick AG at https://github.com/oneclick-ag/python-car-management-api-challenge

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Admin Panel](#admin-panel)

## Features

- **Swagger Documentation (OpenAPI)**

  API documentation is generated using Swagger (OpenAPI) to provide detailed information about available endpoints, request parameters, response formats, and example usage. Explore and interact with the API documentation at `http://localhost:8000/cars/docs`.

- **Throttling**

  Django REST Framework's throttling mechanism is implemented to control the rate of incoming requests. Throttling can be configured in `api/settings.py`.

- **Pagination**

  Pagination is implemented for the `GET /cars` endpoint and works with `limit / offset` GET parameters.

- **Admin Panel**

  Access the Django admin panel from `http://localhost:8000/admin`.

- **Unittests**

  The project includes comprehensive unit tests to ensure functionality and reliability across all API endpoints. Tests cover input validation, error handling, and expected behavior under various scenarios.
  Find the unit tests under `api/tests/`

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/1r00t/car-management-ninja.git
   cd car-management-ninja
   ```

2. **Set up a virtual environment:**

   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Environment Variables

The project uses environment variables to manage settings for development and production environments. By default, it looks for a `.env` file. You can set the `DJANGO_ENV_FILE` variable to switch between `.env.dev` and `.env.prod`.

1. **Create a `.env.dev` file for development:**

   ```ini
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

2. **Create a `.env.prod` file for production:**

   ```ini
   SECRET_KEY=your_production_secret_key
   DEBUG=False
   ALLOWED_HOSTS=your_production_domain
   DATABASE_URL=postgres://user:password@hostname/dbname
   ```

3. **Export `DJANGO_ENV_FILE` environment variable:**
   ```sh
   export DJANGO_ENV_FILE=.env.dev  # For development
   export DJANGO_ENV_FILE=.env.prod  # For production
   ```

## Running the Project

1. **Apply database migrations:**

   ```sh
   python manage.py migrate
   ```

2. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Testing

- **Run the test suite with Django**

  ```sh
  python manage.py test
  ```

- **Or with Pytest**
  ```sh
  pytest
  ```

## Admin Panel

1. **Create a superuser for accessing the admin panel:**

   ```sh
   python manage.py createsuperuser
   ```

2. **Access the admin panel:**

   Open your browser and go to `http://localhost:8000/admin/`.

   Use the superuser credentials to log in.
