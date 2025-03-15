# Asset Management System

This is a Django-based web application for managing assets within an organization. Users can log in, view their assigned assets, and update their profiles.

## Features

- User authentication (login/logout)
- View assigned assets
- View asset details
- Edit user profile
- Admin page for managing users and assets

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/fykhan/asset_management.git
    cd asset_management
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install django
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- **Landing Page**: The main landing page of the application.
- **Login**: Users can log in using their credentials.
- **Assigned Assets**: View the assets assigned to the logged-in user.
- **Asset Details**: View detailed information about a specific asset.
- **Edit Profile**: Update the user's profile information.
- **Admin Page**: Accessible by superusers, the admin page allows for the addition and removal of users and assets.

