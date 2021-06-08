def correct_boolean_values(dictionary: dict):
    for key in dictionary:
        if dictionary[key] == True and type(dictionary[key]) == bool:
            dictionary[key] = "true"
        elif dictionary[key] == False and type(dictionary[key]) == bool:
            dictionary[key] = "false"
    return dictionary

def change_camel_case_to_snake_case(dictionary: dict):
    new_dictionary = dict()
    for key in dictionary.keys():
        new_key = ''.join(['_'+i.lower() if i.isupper() else i for i in key]).lstrip('_')
        new_dictionary[new_key] = dictionary[key]
    
    return new_dictionary