import requests, json

def get_response(target_url="http://jsonplaceholder.typicode.com/users"): 
    get_url = requests.get(str(target_url))
    response = json.loads(get_url.text)
    return response

def response_to_list(response):
    i = 0 
    name_list = []
    for  my_dict in response:
        name_list.append(response[i]["name"])
        i += 1
    return name_list

def response_to_dict(response, dict_key="name"):
    i = 0 
    user_dict = []
    for  all_dict in response:
        user_dict.append(response[i][dict_key])
        i += 1
    return user_dict

# def name_from_list(name_list):
#     i = 0
#     for name in name_list:
#         print(f"index: {i} namn: {name}")
#         i += 1
# TEST
# name_from_list(response_to_list(get_response()))