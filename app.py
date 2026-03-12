@app.route('/student')
def get_student():
    name = request.args.get("name", "Your Name")
    grade = request.args.get("grade", 10)
    section = request.args.get("section", "Zechariah")
    return jsonify({
        "name": name,
        "grade": grade,
        "section": section
    })
