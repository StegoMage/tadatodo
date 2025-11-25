from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import psycopg2.extras
import psycopg2
from database import get_db

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("SELECT * FROM tasks ORDER BY id")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (title) Values (%s)",
                   (title,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    is_complete = data.get("is_complete", False)

    conn = get_db()
    cursor = conn.cursor()

    cursor.exectue("UPDATE tasks SET is_complete = %s WHERE id %s",
                   (is_complete, task_id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Task updated"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)