from datetime import datetime

from flask import Flask, Blueprint, abort, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

#==============
#  UTILS
#==============
tasks = []
api = Blueprint('api', __name__, url_prefix="/api")
def object_as_dict(obj):
    return {
        c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs
    }

#==============
#  APP
#==============
app = Flask(__name__)

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
    description = db.Column(db.String(100), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

#==============
#  API ROUTES
#==============
@api.route('/', methods=['GET'])
def health():
    return jsonify({"message": "Alive"})

@api.route('/todos', methods=['GET'])
def get_todos():
    todos = [object_as_dict(todo) for todo in Todo.query.all()]
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
    
    return jsonify(object_as_dict(todo)), 204

@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    if todo_id is None:
        abort(400)
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(object_as_dict(todo))

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
    return jsonify(object_as_dict(todo))

@api.route('/todos/<int:todo_id>', methods=['PATCH'])
def patch_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(todo, key, value)
    db.session.commit()
    return jsonify(object_as_dict(todo))

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id is None:
        return jsonify({'message': 'Please enter a todo_id'}), 400
    todo = Todo.query.get(todo_id)
    if todo is None:
        return jsonify({'message': 'Todo not found'}), 400
    db.session.delete(todo)
    db.session.commit()
    return jsonify({}), 204

app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
