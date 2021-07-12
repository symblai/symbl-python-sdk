import symbl
import time
import threading

# here you can add more events which support the Streaming API like 'insight_response', 'message_response' etc.
events = {
    'message_response': lambda response: print('Final Messages -> ', [message['payload']['content'] for message in response['messages']])
}

insight_types = ['question', 'action_item']

speaker = {
    'userId': 'John@example.com',
    'name': 'John',
}

connection = symbl.Streaming.start_connection(
    insight_types=insight_types, speaker=speaker)

connection.subscribe(events)

connection.send_audio_from_mic()

# you can get the response from the conversation object, when you will stop the connection explicitly 
# or Python SDK will detect the silence in the on going conversation

print(connection.conversation.get_conversation())
print(connection.conversation.get_messages())
# print(connection.conversation.get_action_items())
# print(connection.conversation.get_follow_ups())
# print(connection.conversation.get_members())
# print(connection.conversation.get_topics())
# print(connection.conversation.get_questions())
