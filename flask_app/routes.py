from flask_app import app

@app.route('/')
def index():
    return "Hej världen!"