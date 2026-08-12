from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.database import db 
from app.models import Task 
from app.schemas import task_schema, tasks_schema

bp = Blueprint('routes', __name__) 


@bp.route('/tasks', methods=['GET'])
def get_tasks(): 
    tasks = Task.query.all()
    return jsonify(tasks_schema.dump(tasks)), 200


@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id): 
    task = Task.query.get_or_404(task_id)
    return jsonify(task_schema.dump(task)), 200


@bp.route('/tasks', methods=['POST'])
def create_task(): 
    data = request.get_json(silent=True)
    if not data: 
        return jsonify({"message": "Nenhum dado enviado."}), 400
    try: 
        validated_data = task_schema.load(data)
    except ValidationError as err: 
        return jsonify(err.messages), 400
    new_task = Task(**validated_data)   
    db.session.add(new_task)
    db.session.commit()

    return jsonify(task_schema.dump(new_task)), 201


@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id): 
    task = Task.query.get_or_404(task_id)
    data = request.get_json(silent=True)
    if not data: 
        return jsonify({"message": "Nenhum dado enviado."}), 400
    try: 
        validated_data = task_schema.load(data, partial=True)
    except ValidationError as err: 
        return jsonify(err.messages), 400
    
    for key, value in validated_data.items(): 
        setattr(task, key, value)
    
    db.session.commit()
    return jsonify(task_schema.dump(task)), 200


@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id): 
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
    
