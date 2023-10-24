from flask_app import app
from flask import jsonify

@app.route('/api/items')
def items():
    my_object = {"user_name": "Richard", "Age": 57}
    return jsonify(my_object)