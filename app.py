from flask import Flask, request, jsonify, render_template, abort
import json
import os
from typing import List, Dict, Any

app = Flask(__name__)

DATA_DIR = 'data'
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')
AUTH_TOKEN = "securetoken"  # Replace with an environment variable in production


def authenticate():
    token = request.headers.get("Authorization")
    if token != AUTH_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401


def load_data(filename: str) -> List[Dict[str, Any]]:
    """Load data from a JSON file."""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
    except json.JSONDecodeError:
        return []
    return []


def save_data(filename: str, data: List[Dict[str, Any]]) -> None:
    """Save data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/library', methods=['GET'])
def library():
    return "Welcome to the Library Management System"


@app.route('/books', methods=['GET'])
def get_books() -> Any:
    """Get books with optional pagination."""
    authenticate()
    books = load_data(BOOKS_FILE)
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    start = (page - 1) * limit
    end = start + limit
    return jsonify(books[start:end])


@app.route('/search_books', methods=['GET'])
def search_books() -> Any:
    """Search books by title or author."""
    authenticate()
    books = load_data(BOOKS_FILE)
    query = request.args.get('query', '').lower()
    results = [book for book in books if query in book.get('title', '').lower() or query in book.get('author', '').lower()]
    return jsonify(results)


@app.route('/students', methods=['GET'])
def get_students() -> Any:
    """Get students with optional pagination."""
    authenticate()
    students = load_data(STUDENTS_FILE)
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    start = (page - 1) * limit
    end = start + limit
    return jsonify(students[start:end])


@app.route('/add_book', methods=['POST'])
def add_book() -> Any:
    """Add a new book."""
    authenticate()
    book = request.json
    books = load_data(BOOKS_FILE)
    
    # Ensure book has an ID before adding
    if 'id' not in book:
        abort(400, 'Book ID is required')
    
    books.append({**book, 'status': 'available'})
    save_data(BOOKS_FILE, books)
    
    return '', 201


@app.route('/remove_book', methods=['DELETE'])
def remove_book() -> Any:
    """Remove a book by ID."""
    authenticate()
    
    book_id = request.json.get('id')
    
    if not book_id:
        abort(400, 'Book ID is required')
    
    books = load_data(BOOKS_FILE)
    
    # Filter out the book to be removed
    updated_books = [book for book in books if book['id'] != book_id]
    
    # Check if any book was removed
    if len(updated_books) == len(books):
        abort(404, 'Book not found')
    
    save_data(BOOKS_FILE, updated_books)
    
    return '', 200


@app.route('/issue_book', methods=['POST'])
def issue_book() -> Any:
    """Issue a book to a student."""
    authenticate()
    
    data = request.json
    book_id = data.get('id')
    
    if not book_id or not data.get('student'):
        abort(400, 'Book ID and student name are required')
    
    books = load_data(BOOKS_FILE)
    
    for book in books:
        if book['id'] == book_id and book['status'] == 'available':
            book['status'] = 'issued'
            book['issued_to'] = data['student']
            save_data(BOOKS_FILE, books)
            return '', 200
    
    abort(400, 'Book not available')


@app.route('/return_book', methods=['POST'])
def return_book() -> Any:
    """Return an issued book."""
    authenticate()
    
    book_id = request.json.get('id')
    
    if not book_id:
        abort(400, 'Book ID is required')
    
    books = load_data(BOOKS_FILE)
    
    for book in books:
        if book['id'] == book_id and book['status'] == 'issued':
            book['status'] = 'available'
            book.pop('issued_to', None)
            save_data(BOOKS_FILE, books)
            return '', 200
    
    abort(400, 'Book not found or not issued')


@app.route('/add_student', methods=['POST'])
def add_student() -> Any:
    """Add a new student."""
    authenticate()
    
    student_name = request.json.get('name')
    
    if not student_name:
        abort(400, 'Student name is required')
        
    students = load_data(STUDENTS_FILE)

    if __name__ == '__main__':
     if not os.path.exists(DATA_DIR):
       os.makedirs(DATA_DIR)
    app.run(debug=True)    
    # Ensure student does not already exist
    if student_name in students:
       abort(400, 'Student already exists')

       students.append(student_name)
       save_data(STUDENTS_FILE, students)
   
       return '', 201




@app.route('/remove_student', methods=['DELETE'])
def remove_student() -> Any:
   """Remove a student."""
   authenticate()
   
   student_name = request.json.get('name')
   
   if not student_name:
       abort(400, 'Student name is required')
   
   students = load_data(STUDENTS_FILE)
   
   # Filter out the student to be removed
   updated_students = [student for student in students if student != student_name]
   
   # Check if any student was removed
   if len(updated_students) == len(students):
       abort(404, 'Student not found')

   save_data(STUDENTS_FILE, updated_students)

   return '', 200


if __name__ == '__main__':
   if not os.path.exists(DATA_DIR):
       os.makedirs(DATA_DIR)
   app.run(debug=True)