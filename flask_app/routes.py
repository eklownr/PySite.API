from flask_app import app
from flask import jsonify

@app.route('/api/items')
def items():
    my_object = {"user_name": "Christian", "age": 29, "id": 1}
    return jsonify(my_object)