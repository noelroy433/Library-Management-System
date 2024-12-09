# Library Management System

## Overview
This project is a simple Library Management System built using Flask, a lightweight web framework for Python. It allows users to manage books and students, including functionalities for adding, removing, issuing, and returning books, as well as managing student records.

## Table of Contents
1. [How to Run the Project](#how-to-run-the-project)
2. [Design Choices Made](#design-choices-made)
3. [Assumptions and Limitations](#assumptions-and-limitations)

## How to Run the Project

### Prerequisites
- Python 3.x
- Flask
- JSON files for data storage

### Steps to Run
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Install Dependencies**
    Make sure you have Flask installed.
    You can install it using pip:
   ```bash
    pip install Flask
3. **Create Data Directory**
   The application requires a data directory to store JSON files for books and students. This will be created automatically when the application runs for the first time.
4. **Run the Application**
   You can run the application using the following command:  
     ```bash
     python app.py
5. Access the Application Open your web browser and navigate to http://127.0.0.1:5000/ to access the Library Management System.     

## Design Choices Made
- Flask Framework: Chosen for its simplicity and ease of use for building web applications.
- JSON for Data Storage: Used JSON files to store books and students data, making it easy to read and write data without the need for a database.
- RESTful API Design: The application follows REST principles, providing clear and consistent endpoints for managing resources (books and students).
- Error Handling: Implemented basic error handling using HTTP status codes to provide feedback on the success or failure of operations.
- Pagination: Added optional pagination for retrieving lists of books and students to improve performance and usability.
- Assumptions and Limitations
- Data Persistence: The application relies on JSON files for data storage, which may not be suitable for large-scale applications or concurrent access. A database would be more appropriate for production use.
- Single User: The current implementation assumes a single user accessing the system at a time. There is no user management or role-based access control.
- Basic Authentication: The authentication mechanism is simplistic and should be replaced with a more secure method (e.g., OAuth) for production environments.
- Limited Functionality: The application provides basic functionalities and does not include advanced features like search filters, sorting, or user notifications.
- Error Handling: While basic error handling is implemented, it may not cover all edge cases, and further improvements could be made.
## Conclusion
This Library Management System serves as a foundational project for managing books and students. It can be extended with additional features and improvements based on the outlined limitations and design choices.
   
