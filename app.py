
from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Home endpoint
@app.route('/')
def home():
    return "Welcome to my first API!"

# 2. Student endpoint
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "2026-00123",
        "name": "Juan Dela Cruz",
        "program": "BSIT",
        "year": 1,
        "section": "A"
    })

# 3. Greeting endpoint
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
