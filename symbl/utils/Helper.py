import json
from symbl import AuthenticationToken
import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

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

#verify date format
def verify_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

#Parse date format
def deserialize_date(strISODateString):
    """Deserializes string to date.
    :param strISODateString: str.
    :return: date.
    """
    try:
        from datetime import datetime
        return datetime.strptime(strISODateString, DATE_FORMAT)
    except ImportError:
        return strISODateString
    except ValueError:
        raise Exception(
            status=0,
            reason="Failed to parse `{0}` as date object".format(strISODateString)
        )

#This function will remove the None values from the API response, and will also parse the date format
def parse_entity_response(api_response):
    api_response=api_response.entities
    count = len(api_response)
    entity_response=[]

    keys = ['custom_type','end','message_refs','start','type','text','value']

    for obj in range(0,count):
        entity_res = dict()
        for key in keys:
            val = getattr(api_response[obj],key)
            if val is not None:
                if key=='value': 
                    if verify_date(val):
                        val = "".join([val," 00:00:00"])
                        val = deserialize_date(val)
                entity_res[key]=val
        entity_response.append(entity_res) 

    return dict(entities=entity_response)