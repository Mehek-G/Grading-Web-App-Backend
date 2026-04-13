from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

grades = {}

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def serve_css():
    return send_from_directory(".", "style.css")

@app.route("/script.js")
def serve_js():
    return send_from_directory(".", "script.js")

# get all grades
@app.route("/grades", methods=["GET"])  # <-- ADDED
def get_all_grades():
    return jsonify(grades)

# Get one grade
@app.route("/grades/<name>", methods=["GET"])
def get_grades(name):
    if name in grades:
        return jsonify({name: grades[name]})
    else:
        return jsonify({"error": "Student not found"}), 404
    
# add new student
@app.route("/grades", methods=["POST"])
def add_grade():
    data = request.get_json()

    name = data["name"]
    grade = data["grade"]
    grades[name] = grade

    return jsonify({"message": "Added successfully"})

# edit grade
@app.route("/grades/<name>", methods=["PUT"])
def edit_grade(name):
    if name not in grades:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    grades[name] = data["grade"]

    return jsonify({"message": "Updated successfully"})

# delete grade
@app.route("/grades/<name>", methods=["DELETE"])
def delete_grade(name):
    if name not in grades:
        return jsonify({"error": "Student not found"}), 404

    del grades[name]

    return jsonify({"message": "Deleted successfully"})

# run app
if __name__ == "__main__":
    app.run(debug=True)