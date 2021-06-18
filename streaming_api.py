import symbl

events = {
    'message_response': lambda response: print('Final Messages -> ', [ message['payload']['content'] for message in response['messages']])
}

connection = symbl.Streaming.start_connection(insight_types=['question', 'action_item'], speaker={'name': 'Roshani', 'email': 'roshani.jawale@symbl.ai'})

connection.subscribe(events)
connection.send_audio_from_mic()

print(connection.conversation.get_conversation_data())