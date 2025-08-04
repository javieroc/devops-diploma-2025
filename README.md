# Book Catalog API

This is a simple Book Catalog API built with Django and Django REST Framework, developed as the capstone project for the DevOps Diploma 2025.

## Project Overview

The goal of this project is to design, build, and deploy a RESTful API for managing a book collection. The project includes the API itself, automated tests, containerization with Docker, and a CI/CD pipeline for automated builds, testing, and deployment to a Kubernetes cluster using Helm.

## API Usage Examples

The following endpoints are available:

*   `GET /api/health/`: Health check endpoint.
*   `GET /api/books/`: Retrieve a list of all books.
*   `POST /api/books/`: Create a new book.
*   `GET /api/books/{id}/`: Retrieve a single book by its ID.
*   `PUT /api/books/{id}/`: Update a book's details.
*   `DELETE /api/books/{id}/`: Delete a book.

### Example using cURL:

**Get all books:**

```bash
curl http://localhost:8000/api/books/
```

**Create a new book:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "isbn": "978-0-618-64015-7",
    "published_date": "1954-07-29"
}' http://localhost:8000/api/books/
```

## Local Build and Run Instructions

To run the application locally, you need Docker and Docker Compose.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/connan-sensei/devops-diploma-2025.git
    cd devops-diploma-2025
    ```

2.  **Build and run the application:**
    ```bash
    docker-compose up -d --build
    ```

The API will be available at `http://localhost:8000`.

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/test.yml` and includes the following jobs:

*   **test**: Installs dependencies and runs the unit tests.
*   **runmigrations**: Runs Django database migrations.
*   **migrations-check**: Checks for any missing migrations.
*   **semantic-release**: Automatically creates a new release and changelog entry when changes are merged to the `main` branch.
*   **build-docker-image**: Builds and pushes a new Docker image to the GitHub Container Registry when a new release is published.

## Kubernetes and Helm Setup

The application can be deployed to a Kubernetes cluster using the Helm chart located in the `books-catalog-chart` directory.

**Prerequisites:**

*   A running Kubernetes cluster.
*   `kubectl` configured to connect to your cluster.
*   Helm installed.

**Deployment Steps:**

1.  **Create a secret for the GitHub Container Registry:**
    ```bash
    kubectl create secret docker-registry ghcr-token --docker-server=ghcr.io --docker-username=<YOUR_GITHUB_USERNAME> --docker-password=<YOUR_GITHUB_TOKEN>
    ```

2.  **Install the Helm chart:**
    ```bash
    helm install my-release ./books-catalog-chart
    ```

This will deploy the application to your Kubernetes cluster. You can customize the deployment by modifying the `values.yaml` file in the `books-catalog-chart` directory.
