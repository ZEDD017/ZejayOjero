from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Sample student data storage
students = [
    {"name": "John Doe", "grade": 10, "section": "Zechariah"},
    {"name": "Jane Smith", "grade": 11, "section": "Gabriel"}
]

# ----------------------
# Home page with animated background
# ----------------------
@app.route('/')
def home():
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>ZEJAY POGI App</title>
        <style>
            @keyframes gradient {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
                background-size: 400% 400%;
                animation: gradient 15s ease infinite;
                color: #333;
                text-align: center;
                padding: 50px;
                overflow-x: hidden;
            }

            h1 { color: #ff6b6b; margin-bottom: 20px; }

            a.button {
                background: #1dd1a1;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 8px;
                margin: 10px;
                display: inline-block;
                font-weight: bold;
                transition: 0.3s;
            }
            a.button:hover { background: #10ac84; }

            ul { list-style: none; padding: 0; }
            li { margin: 8px 0; padding: 8px; background: rgba(255, 255, 255, 0.8); border-radius: 6px; width: 300px; margin-left: auto; margin-right: auto; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);}
            
            /* Floating bubbles */
            .bubble {
                position: absolute;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.2);
                animation: float 10s infinite;
            }

            @keyframes float {
                0% { transform: translateY(100vh) scale(0.5); opacity: 0;}
                50% { opacity: 0.7; }
                100% { transform: translateY(-10vh) scale(1); opacity: 0;}
            }
        </style>
    </head>
    <body>
        <h1>Hi ZEJAY POGI, Your App is Running!</h1>
        <p>Here is the list of students:</p>
        <ul>
            {% for student in students %}
                <li>{{ student.name }} - Grade {{ student.grade }}, Section {{ student.section }}</li>
            {% endfor %}
        </ul>
        <a class="button" href="{{ url_for('add_student_form') }}">Add New Student</a>

        <!-- Floating bubbles -->
        {% for i in range(15) %}
            <div class="bubble" style="width: {{ 20 + i*5 }}px; height: {{ 20 + i*5 }}px; left: {{ (i*7)%100 }}%; animation-delay: {{ i }}s;"></div>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(template, students=students)

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
# HTML Form to Add Student (embedded)
# ----------------------
@app.route('/add-student', methods=['GET', 'POST'])
def add_student_form():
    if request.method == 'POST':
        name = request.form.get("name")
        grade = request.form.get("grade")
        section = request.form.get("section")
        if not name or not grade or not section:
            error = "All fields are required!"
        else:
            student = {"name": name, "grade": int(grade), "section": section}
            students.append(student)
            return redirect(url_for('home'))
    else:
        error = None

    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Add Student</title>
        <style>
            body { font-family: Arial; background: #f4f4f4; text-align: center; padding: 50px; }
            form { background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0px 4px 8px rgba(0,0,0,0.1); }
            input { padding: 12px; margin: 8px 0; width: 250px; border-radius: 6px; border: 1px solid #ccc; }
            button { padding: 12px 25px; background: #ff6b6b; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s; }
            button:hover { background: #ee5253; }
            .error { color: red; margin-bottom: 10px; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>Add a New Student</h1>
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
        <form method="POST">
            <input type="text" name="name" placeholder="Name" required><br>
            <input type="number" name="grade" placeholder="Grade" required><br>
            <input type="text" name="section" placeholder="Section" required><br>
            <button type="submit">Add Student</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(template, error=error)

# ----------------------
# Run the app
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
