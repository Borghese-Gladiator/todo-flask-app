from flask import Flask, render_template, redirect, url_for
from models import Task  # Import Task from models.py

app = Flask(__name__)

# Placeholder for tasks, can be replaced by a database
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add-task/<description>')
def add_task(description):
    new_task = Task(description)
    tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/delete-task/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/update-task/<int:task_id>/<description>')
def update_task(task_id, description):
    if task_id < len(tasks):
        tasks[task_id].description = description
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
