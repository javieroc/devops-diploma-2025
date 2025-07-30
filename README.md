# Book Catalog API

This is a simple Book Catalog API built with Django and Django REST Framework.

## API Usage Examples

### List all books

```bash
curl http://localhost:8000/api/books/
```

### Get a single book

```bash
curl http://localhost:8000/api/books/1/
```

### Create a new book

```bash
curl -X POST -H "Content-Type: application/json" -d '
{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "isbn": "978-0-618-64015-7",
    "published_date": "1954-07-29"
}' http://localhost:8000/api/books/
```

### Update a book

```bash
curl -X PUT -H "Content-Type: application/json" -d '
{
    "title": "The Hobbit"
}' http://localhost:8000/api/books/1/
```

### Delete a book

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

## Local Build and Run Instructions

To build and run the project locally, you need to have Docker and Docker Compose installed.

1.  Clone the repository:

    ```bash
    git clone https://github.com/connan-sensei/devops-diploma-2025.git
    cd devops-diploma-2025
    ```

2.  Build and run the containers:

    ```bash
    docker-compose up -d --build
    ```

3.  The API will be available at `http://localhost:8000/api/`.
