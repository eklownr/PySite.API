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