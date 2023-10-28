import requests, json

def get_response(target_url="http://jsonplaceholder.typicode.com/users"): 
    get_url = requests.get(str(target_url))
    response = json.loads(get_url.text)
    return response

def response_to_list(response):
    i = 0 
    name_list = []
    for person_dict in response:
        name_list.append(response[i]["name"])
        i += 1
    return name_list

def response_to_dict(response, dict_key="name"):
    ''' return dict{ id: name } '''
    user_dict = {}
    for all_dict in response:
        user_dict[all_dict["id"]] = all_dict[dict_key]
    return user_dict

# TEST
# print(response_to_dict(get_response()))

def get_persons():
    persons = {
        1: 'Leanne Graham',
        2: 'Ervin Howell', 
        3: 'Clementine Bauch', 
        4: 'Patricia Lebsack', 
        5: 'Chelsey Dietrich', 
        6: 'Mrs. Dennis Schulist', 
        7: 'Kurtis Weissnat', 
        8: 'Nicholas Runolfsdottir V', 
        9: 'Glenna Reichert', 
        10: 'Clementina DuBuque',
    }
    return persons

def get_potter_list():
    potters = [
        {"id": 1, "name": "Minerva McGonagall"},
        {"id": 2, "name": "Luna Lovegood"},
        {"id": 3, "name": "Hermione Granger"},
        {"id": 4, "name": "Rubeus Hagrid"},
        {"id": 5, "name": "Sirius Black"}, 
        {"id": 6, "name": "Harry Potter"},  
        {"id": 7, "name": "Albus Dumbledore"},  
        {"id": 8, "name": "Severus Snape"},
        {"id": 9, "name": "Sirius Black"}, 
        {"id": 10, "name": "Neville Longbottom"},   
        {"id": 11, "name": "Dobby"},
        {"id": 12, "name": "Ginny Weasley"},   
        {"id": 13, "name": "Draco Malfoy"}, 
        {"id": 14, "name": "Bellatrix Lestrange"},  
        {"id": 15, "name": "Ronald Weasley"},
        # Alastor Moody
    ]
    return potters
