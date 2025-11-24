# Bookstore Management Web Server

This project is a **Python-based web server** for managing a bookstore. It implements a basic HTTP server and handles requests for books, customers, orders, order items, and static files. It also includes a MySQL database with sample data and schema.

## Features

- CRUD operations for:
  - Books
  - Customers
  - Orders
  - Order items
- Automatic order total calculation via MySQL trigger
- Serving static files (HTML, CSS, JS, images)
- SCSS compilation to CSS
- Lightweight HTTP server using Python's `http.server`
- Simple URL routing to controllers and actions
- Multi-threaded server with automatic browser launch

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.13+
- `mysql-connector-python` for database access
- `libsass` or `pysass` for SCSS compilation

Install dependencies:
```bash
pip install mysql-connector-python
pip install libsass
```

### Run the Project

Open a terminal in the project root directory and run:

Starting Docker Container
```bash
docker-compose up --build
```
Start the Python HTTP server:
```bash
python main.py
```
The server will run on http://localhost:8000. The main page will automatically open in your default web browser.

