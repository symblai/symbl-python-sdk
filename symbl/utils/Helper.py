import json
from symbl import AuthenticationToken


def correct_boolean_values(dictionary: dict):
    for key in dictionary:
        if dictionary[key] == True and type(dictionary[key]) == bool:
            dictionary[key] = "true"
        elif dictionary[key] == False and type(dictionary[key]) == bool:
            dictionary[key] = "false"
    return dictionary

def dictionary_to_valid_json(dictionary: dict):
    new_dictionary = dict()
    for key in dictionary.keys():
        new_key = ''.join(['_'+i.lower() if i.isupper() else i for i in key]).lstrip('_')
        if type(dictionary[key]) == list or type(dictionary[key]) == dict:
            new_dictionary[new_key] = json.dumps(dictionary[key])
        else:
            new_dictionary[new_key] = dictionary[key]
    
    return new_dictionary

def initialize_api_client(function):
    def wrapper(*args, **kw):
        credentials = None
        
        if 'credentials' in kw:
            credentials = kw['credentials']

        AuthenticationToken.get_api_client(credentials)

        return function(*args, **kw)
    
    return wrapper