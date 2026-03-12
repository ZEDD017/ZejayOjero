from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi ZEJAY POGI, Your app is running!"

# GET endpoint with default student data
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# GET endpoint with query parameters
@app.route('/student/query', methods=['GET'])
def get_student_query():
    name = request.args.get("name", "Your Name")
    grade = request.args.get("grade", 10)
    section = request.args.get("section", "Zechariah")
    return jsonify({
        "name": name,
        "grade": grade,
        "section": section
    })

# POST endpoint to accept JSON data
@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify({
        "message": "Student added successfully!",
        "student": data
    })

if __name__ == "__main__":
    app.run(debug=True)

