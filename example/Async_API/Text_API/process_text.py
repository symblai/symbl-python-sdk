import symbl

#you can add the different vocabulary, which you would like to track
trackers = [{
    "name": "text_tracker",
    "vocabulary": [
        "white",
        "issues",
        "vaccination"
    ]
}]
payload = {
    
    "name": "TextAPI",  # you can update the name of the conversation

    "features": {
        "featureList": [
            "insights",
            "callScore"
        ]
    },
    "metadata": {
        "salesStage": "qualification",
        "prospectName": "DeepMind AI"
    },
    
    #"trackers": trackers,  #To detect the trackers
    
    #"detectEntities": "true", #To get the entities
    
    #To define Custom entities
    "entities": [
        {
            "customType": "identify_org",
            "text": "platform"
        }
    ],
    "messages": [
        {
            "payload": {"content": "Hi Anthony. I saw your complaints about bad call reception on your mobile phone. Can I know what issues you are currently facing?"},
            "from": {"userId": "surbhi@example.com", "name": "Surbhi Rathore"}
        },
        {
            "payload": {"content": "Hey Surbhi, thanks for reaching out. Whenever I am picking up the call there is a lot of white noise and I literally can’t hear anything."},
            "from": {"userId": "anthony@example.com", "name": "Anthony Claudia"}
        },
        {
            "payload": {"content": "Okay. I can schedule a visit from one of our technicians for tomorrow afternoon at 1:00 PM. He can look at your mobile and handle any issue right away"},
            "from": {"userId": "surbhi@example.com", "name": "Surbhi Rathore"}
        },
        {
            "payload": {"content": "That will be really helpful. I'll follow up with the technician about some other issues too, tomorrow"},
            "from": {"userId": "anthony@example.com", "name": "Anthony Claudia"}
        },
        {
            "payload": {"content": "Sure. We are happy to help. I am scheduling the visit for tomorrow. Thanks for using Abccorp networks. Have a good day."},
            "from": {"userId": "surbhi@example.com", "name": "Surbhi Rathore"}
        }
    ]
}

conversation_object = symbl.Text.process(payload=payload)

# To get the message from the conversation
print(conversation_object.get_messages())
print(conversation_object.get_call_score_status())

#To get the conversation data from the conversation
#print(conversation_object.get_conversation())

# To get the action items from the conversation
# print(conversation_object.get_action_items())

# To get the follow ups from the conversation
# print(conversation_object.get_follow_ups())

# To get the members information from the conversation
# print(conversation_object.get_members())

# To get the topics from the conversation
# print(conversation_object.get_topics())

# To get the questions from the conversation
# print(conversation_object.get_questions())

# To get the analytics from the conversation
#print(conversation_object.get_analytics())

# To get the trackers from the conversation
#print(conversation_object.get_trackers())

# To get the entities from the conversation
#print(conversation_object.get_entities())