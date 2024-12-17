
# Social Media API

This project is a Social Media API built with Django and Django REST Framework. It includes user authentication, and functionalities for creating, viewing, updating, and deleting posts and comments.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/social_media_api.git
    cd social_media_api
    ```

2. **Set Up a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

## User Authentication

### Registration

- **Endpoint:** `/accounts/register/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "username": "your_username",
      "email": "your_email",
      "password": "your_password",
      "bio": "Your bio",
      "profile_picture": "url_to_profile_picture"
    }
    ```
- **Response:**
    ```json
    {
      "token": "user_auth_token"
    }
    ```

### Login

- **Endpoint:** `/accounts/login/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
      "token": "user_auth_token"
    }
    ```

## Posts and Comments

### Create a Post

- **Endpoint:** `/posts/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "title": "Post Title",
      "content": "Post Content"
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "author": "user_id",
      "title": "Post Title",
      "content": "Post Content",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

### Create a Comment

- **Endpoint:** `/comments/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "post": "post_id",
      "content": "Comment Content"
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "post": "post_id",
      "author": "user_id",
      "content": "Comment Content",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

## Follow and Feed

### Follow a User

- **Endpoint:** `/accounts/follow/<user_id>/`
- **Method:** `POST`
- **Response:**
    ```json
    {
      "message": "User followed"
    }
    ```

### Unfollow a User

- **Endpoint:** `/accounts/unfollow/<user_id>/`
- **Method:** `POST`
- **Response:**
    ```json
    {
      "message": "User unfollowed"
    }
    ```

### Get Feed

- **Endpoint:** `/feed/`
- **Method:** `GET`
- **Response:**
    ```json
    [
      {
        "id": 1,
        "author": "user_id",
        "title": "Post Title",
        "content": "Post Content",
        "created_at": "timestamp",
        "updated_at": "timestamp",
        "comments": [
          {
            "id": 1,
            "post": "post_id",
            "author": "user_id",
            "content": "Comment Content",
            "created_at": "timestamp",
            "updated_at": "timestamp"
          }
        ]
      }
    ]
    ```
# Social Media API

This project is a Social Media API built with Django and Django REST Framework. It includes user authentication, and functionalities for creating, viewing, updating, and deleting posts and comments, as well as following users and viewing an aggregated feed of posts.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/social_media_api.git
    cd social_media_api
    ```

2. **Set Up a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

## User Authentication

### Registration

- **Endpoint:** `/api/accounts/register/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "username": "your_username",
      "email": "your_email",
      "password": "your_password",
      "bio": "Your bio",
      "profile_picture": "url_to_profile_picture"
    }
    ```
- **Response:**
    ```json
    {
      "token": "user_auth_token"
    }
    ```

### Login

- **Endpoint:** `/api/accounts/login/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
      "token": "user_auth_token"
    }
    ```

## Posts and Comments

### Create a Post

- **Endpoint:** `/api/posts/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "title": "Post Title",
      "content": "Post Content"
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "author": "user_id",
      "title": "Post Title",
      "content": "Post Content",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

### Create a Comment

- **Endpoint:** `/api/comments/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "post": "post_id",
      "content": "Comment Content"
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "post": "post_id",
      "author": "user_id",
      "content": "Comment Content",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

## Follow and Feed

### Follow a User

- **Endpoint:** `/api/accounts/follow/<user_id>/`
- **Method:** `POST`
- **Response:**
    ```json
    {
      "message": "User followed"
    }
    ```

### Unfollow a User

- **Endpoint:** `/api/accounts/unfollow/<user_id>/`
- **Method:** `POST`
- **Response:**
    ```json
    {
      "message": "User unfollowed"
    }
    ```

### Get Feed

- **Endpoint:** `/api/feed/`
- **Method:** `GET`
- **Response:**
    ```json
    [
      {
        "id": 1,
        "author": "user_id",
        "title": "Post Title",
        "content": "Post Content",
        "created_at": "timestamp",
        "updated_at": "timestamp",
        "comments": [
          {
            "id": 1,
            "post": "post_id",
            "author": "user_id",
            "content": "Comment Content",
            "created_at": "timestamp",
            "updated_at": "timestamp"
          }
        ]
      }
    ]
    ```

## License

This project is licensed under the MIT License.

