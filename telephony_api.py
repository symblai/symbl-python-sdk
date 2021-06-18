
import symbl

data = {
    "session": {
        "name": "My Meeting"
    }
}

connection = symbl.Telephony.start_sip(uri="sip:8002@sip.rammer.ai", data=data)
events = {
    'transcript_response': lambda transcript: print('printing the first response ', str(transcript))
}
connection.subscribe(events)
print(connection.conversation.get_conversation_data())

'''
#-----------------------------------------------------------------------------------------------------------------------------#
connection = symbl.Telephony.start_pstn(phone_number="+13017158592", dtmf=",,83313098855#,,108921#", actions={})
events = {
        'transcript_response': lambda response: print('printing the first response ' + str(response)), 
        'insight_response': lambda response: print('printing the first response ' + str(response))
        }
connection.subscribe(events)

print(connection.conversation.get_conversation_data())
'''
