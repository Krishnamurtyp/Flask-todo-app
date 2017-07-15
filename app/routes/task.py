"""
.. module:: task
    :synopsis: All routes on the ``task`` Blueprint.

.. moduleauthor:: Aaron Scheu
"""

from flask import Blueprint, render_template, jsonify, request
import datetime
from app.models import Task, db

task = Blueprint('task', __name__)


@task.route('/', methods=['GET'])
def index():
    """Render main view
        :returns text/html document
    """
    return render_template('index.html')


@task.route('/about', methods=['GET'])
def about():
    """Render my about page
        :returns text/html document
    """
    return render_template('about.html')


@task.route('/list', methods=['GET'])
def get_entries():
    """Get all todo items
        :rtype json
    """
    data = [Task.as_dict(e) for e in Task.query.all()]
    return jsonify(data)


@task.route('/add', methods=['POST'])
def add_entry():
    """Add new todo item to db
        :param json with ['due', 'title', 'description']
        :returns code 201, success or Error
    """
    res = request.get_json(force=True)
    entry = Task(datetime.datetime.strptime(res.get('due'), '%Y-%m-%d').date(), res.get('title'), res.get('description'))
    db.session.add(entry)
    db.session.commit()
    return jsonify({'msg': 'success', 'added': Task.as_dict(entry)}), 201


@task.route('/delete', methods=['POST'])
def delete_entry():
    """Delete item based on id
        :param json with entry id
    """
    id = request.get_json(force=True).get('id')
    entry = Task.query.filter_by(id=id).first()
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'msg': 'success'}), 200


@task.route('/update', methods=['POST'])
def update_entry():
    """Update route to change the state of an item
        :param json with state object
    """
    req = request.get_json(force=True)
    entry = Task.query.filter_by(id=req.get('id')).first()
    entry.state = req.get('state')
    db.session.commit()
    return jsonify({'msg': 'success'}), 200
