from flask_app import app
from flask import jsonify
from . api_helper import get_response, response_to_list

@app.route('/api/items')
def items():
    my_object = {"user_name": "Christian", "age": 29, "id": 1}
    return jsonify(my_object)

@app.route('/api/add')
def add_user():
    pass

@app.route('/api/del')
def del_user():
    pass

@app.route('/api/mod')
def mod_user():
    pass

@app.route('/api/view')
def view_users():
    user_name = response_to_list(get_response())
    return jsonify(user_name)
