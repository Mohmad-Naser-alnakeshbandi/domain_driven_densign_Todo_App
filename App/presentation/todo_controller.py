# App/controllers/todo_controller.py
from flask import Flask, jsonify, request
from App.application.todo_service import TodoService
from App.infrastructure.todo_repository import TodoRepository
from App.database import db_path

app = Flask(__name__)
todo_repo = TodoRepository(db_path)
todo_service = TodoService(todo_repo)

@app.route('/todos', methods=['POST'])
def add_a_todo():
    content = request.json['content']
    status = request.json['status']
    todo_service.add_todo(content,status)
    return jsonify({"message": "Todo added successfully!"}), 201

@app.route('/todos', methods=['GET'])
def get_all_todo():
    all_todos = todo_service.get_all_todos()
    return jsonify(all_todos), 200

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_a_todo_status(todo_id: int):
    todo_status = request.json['status']
    todo_service.update_a_todo_status(todo_id, todo_status)
    return jsonify({"message": "Todo content updated successfully!"}), 200

@app.route('/todos', methods=['DELETE'])
def delete_a_todo():
    id = request.json['id']
    todo_service.delete_a_todo(id)
    return jsonify({"message": "Todo deleted successfully!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
