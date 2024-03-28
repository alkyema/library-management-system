# Library Management System README

## Overview

This Python script provides a simple console-based Library Management System that facilitates managing books, admins, and student records in a library. The system allows for operations such as adding or deleting books, students, and admins, issuing and returning books, and searching for books based on various criteria.

## Prerequisites

To run this script, you will need:

- Python installed on your system.
- MySQL server running locally or remotely with access credentials.
- `mysql-connector-python` package installed to connect to the MySQL database.
- `keyboard` package installed for simulating keyboard inputs.

You can install the required Python packages using pip:

```bash
pip install mysql-connector-python keyboard
```

## Database Setup

Before running the script, ensure your MySQL database is set up with the necessary tables. The script assumes the following table structure:

1. `ad_id` for admin records:
   - `id` (INT) - Admin ID
   - `name` (VARCHAR) - Admin Name
   - `password` (VARCHAR) - Admin Password

2. `st_id` for student records:
   - `id` (INT) - Student ID
   - `name` (VARCHAR) - Student Name
   - `password` (VARCHAR) - Student Password
   - `book1` (INT) - First issued book ID
   - `book2` (INT) - Second issued book ID
   - `book3` (INT) - Third issued book ID

3. `books` for book records:
   - `Book_id` (INT) - Book ID
   - `Name` (VARCHAR) - Book Name
   - `Author` (VARCHAR) - Author's Name
   - `Price` (INT) - Book Price
   - `Quantity` (INT) - Quantity available

Make sure to adjust the database connection parameters in the script to match your MySQL server configuration:

```python
mydb = mysql.connector.connect(
    host="localhost", user="root", password="yourpassword", database="library"
)
```

## Features

The system supports the following features:

- **Admin and Student Login**: Separate login functionalities for admin and students.
- **Admin Features**:
  - View admin and student lists.
  - Add or delete admins and students.
  - Add, delete, or edit book records.
  - Search for books based on name, ID, author, or price range.
  - Change own password or name.
- **Student Features**:
  - View available books.
  - Search for books.
  - Issue or return books (up to 3 at a time).
  - View issued books.
  - Change own username or password.

## Running the Script

To run the script, navigate to the directory where the script is saved and execute the following command:

```bash
python libary.py
```

## Caution

This script is designed for educational purposes and demonstrates basic database operations. It's important to handle user inputs securely and validate them before executing SQL queries in a production environment to prevent SQL injection attacks. 

Always ensure that your application complies with the best practices for security and data protection.
