def isEmpty(value):
    return value == None or len(value) == 0

def validateActions(actions):
    invalidActions = []
    for action in actions:
        if isEmpty(action["invokeOn"]) and isEmpty(action["name"]):
            invalidActions.append(action)
        
    if len(invalidActions) > 0 :
        raise ValueError({'message': "Invalid actions detected. Count: ${invalidActions.length}", "actions": invalidActions})

def validateEndpoint(endpoint):
    if isEmpty(endpoint["type"]):
        raise ValueError("endpoint type is required.")
    
    if endpoint["type"].lower() == "pstn":
        if isEmpty(endpoint["phoneNumber"]):
            raise ValueError("phoneNumber is required when type = 'pstn'.")
    
    elif endpoint["type"].lower() == "sip":
        if isEmpty(endpoint["uri"]):
            raise ValueError("uri is required when type = 'sip'.")
    
    else:
        raise ValueError("endpoint.type = '${endpoint.type}' is not valid. Supported types are ['pstn' , 'sip']")