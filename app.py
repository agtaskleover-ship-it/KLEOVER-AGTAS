
from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Home endpoint
@app.route('/')
def home():
    return "Welcome to Kleover's API!"

# 2. Student details endpoint
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00143",
        "name": "KLEOVER AGTAS",
        "program": "BSIT",
        "year": 3,
        "section": "HAMILTON"
    })

# 3. Greeting endpoint
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

# 4. New endpoint: My Hobby
@app.route('/my-hobby')
def my_hobby():
    return jsonify({
        "name": "KLEOVER AGTAS",
        "hobby": "Reading",
        "description": "I enjoy reading books during my free time."
    })

# 5. New endpoint: Study Plan
@app.route('/study-plan')
def study_plan():
    subject = request.args.get('subject', 'Information Technology')
    return jsonify({
        "student": "KLEOVER AGTAS",
        "subject": subject,
        "study_tip": f"Review your notes and practice exercises in {subject}.",
        "goal": "Understand the lesson and complete all activities."
    })

if __name__ == '__main__':
    app.run(debug=True)
