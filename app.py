from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

# Sample student data storage
students = [
    {"name": "John Doe", "grade": 10, "section": "Zechariah"},
    {"name": "Jane Smith", "grade": 11, "section": "Gabriel"}
]

# ----------------------
# Home page (HTML)
# ----------------------
@app.route('/')
def home():
    return render_template("home.html", title="ZEJAY POGI App")

# ----------------------
# GET endpoint with default student data
# ----------------------
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify(students)

# ----------------------
# GET endpoint with query parameters
# ----------------------
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

# ----------------------
# POST endpoint to accept JSON data
# ----------------------
@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    students.append(data)
    return jsonify({
        "message": "Student added successfully!",
        "student": data
    })

# ----------------------
# HTML Form to Add Student
# ----------------------
@app.route('/add-student', methods=['GET', 'POST'])
def add_student_form():
    if request.method == 'POST':
        name = request.form.get("name")
        grade = request.form.get("grade")
        section = request.form.get("section")
        if not name or not grade or not section:
            return render_template("add_student.html", error="All fields are required!")
        student = {"name": name, "grade": int(grade), "section": section}
        students.append(student)
        return redirect(url_for('home'))
    return render_template("add_student.html")

# ----------------------
# Run the app
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
