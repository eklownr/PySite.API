from flask_app import app
from flask import jsonify, render_template, request
from . api_helper import *
from datetime import datetime


@app.route('/api/items')
def items():
    my_object = {"user_name": "Adam", "age": 29, "id": 1}
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
    ''' return id and name as a dict '''
    persons = get_persons()
    return persons

@app.route('/api/potter') 
def potter():
    ''' return id and name as a list of potter characters '''
    potter_list = get_potter_list()
    return jsonify(potter_list)

# TEST update person-name with id
person = [
    {"id": 1, "name": "eva"},
    {"id": 2, "name": "adam"},
]

@app.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    found = False
    for p in person:
        if p['id'] == id:
            p['name'] = request.form['name']
            found = True
            break

    if not found:
        return 'Person not found', 404

    return 'Person updated'
# TEST END


# HTMX via flask
@app.route('/')
def base():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-1]
    subreddit = response["subreddit"]
    title = response["title"]
    return meme_large, subreddit, title

@app.route('/meme')
def meme():
    meme_pic, subreddit, title = get_meme()
    return render_template("meme.html", meme_pic=meme_pic, subreddit=subreddit, title=title) 

@app.route('/api/update', methods=['POST'])
def update():
    name = request.form.get('name')
    return f'<p>Hello, {name}! <a href="/meme"> watch this meme! </a></p>'

@app.route("/info", methods=['POST', 'GET'])
def info():
    now = datetime.now()
    return f'<h3>{now.hour}:{now.minute}:{now.second} <h3/>'

@app.route('/potters')
def potters():
    potter_characters = get_potter_list()
    return render_template('potters.html', potter_characters=potter_characters)

@app.route('/api/add_potters', methods=['POST'])
def add_potters():
    name = request.form.get('name')
    return f'<p>New name: {name}! </p>'

@app.route('/about')
def about():
    return render_template('about.html')
