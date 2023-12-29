from datetime import datetime

from flask import Flask, Blueprint, abort, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#==============
#  STORAGE
#==============
tasks = []

#==============
#  APP
#==============
app = Flask(__name__)
api = Blueprint('api', __name__, url_prefix='/api')

# Configure
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#==============
#  MODELS
#==============
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@api.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify(todos)

@api.route('/todos/', methods=['POST'])
def create_todo():
    todo_data = request.get_json()
    if 'title' not in todo_data or 'description' not in todo_data:
        return jsonify({"error": "Title and description are required fields."}), 400
    if not isinstance(todo_data['title'], str) or not isinstance(todo_data['description'], str):
        return jsonify({"error": "Title and description must be strings."}), 400
    todo = Todo(title=todo_data['title'], description=todo_data['description'])
    db.session.add(todo)
    db.session.commit()
    
    return jsonify(todo, 204)

@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo():
    todo_id = request.args.get('todo_id')
    if todo_id is None:
        abort(400)
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo is None:
        abort(404)
    return jsonify(todo), 200

@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404

    data = request.get_json()
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)

    db.session.commit()
    return jsonify(todo), 200

@api.route('/todos/<int:todo_id>', methods=['PATCH'])
def patch_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(todo, key, value)
    db.session.commit()
    return jsonify(todo), 200

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo():
    todo_id = request.args.get('todo_id')
    if todo_id is None:
        abort(400)
    with db.session.begin() as session:
        todo = session.query(Todo).filter_by(id=todo_id).first()
        if todo is None:
            abort(404)
        db.session.delete(todo)
        db.session.commit()
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True)
