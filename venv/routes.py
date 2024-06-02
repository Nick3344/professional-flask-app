from flask import current_app as app
from flask import jsonify, request
from .models import User, db

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added!'}), 201
