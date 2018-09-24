from flask import Blueprint, jsonify

users_bluepoint = Blueprint('users', __name__)


@users_bluepoint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({'status': 'success', 'message': 'pong!'})
