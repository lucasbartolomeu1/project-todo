from flask import Blueprint, request, jsonify
from app.database import db 
from app.models import Task 

bp = Blueprint('routes', __name__) 

@bp.route('/tasks', methods=['GET'])
def get_tasks(): 
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id): 
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@bp.route('/tasks', methods=['POST'])
def create_task(): 
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description'))
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id): 
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id): 
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
    
