import symbl
events = {
    'message': lambda response: print(response),
    'message_response': lambda response: print('Final Messages -> ', [ message['payload']['content'] for message in response['messages']])
}
connection_object = symbl.Streaming.start_connection(insight_types=['question', 'action_item'],speaker= {
 'userId': 'abc@example.com',
      'name': 'abc',
    })
connection_object.subscribe(events)

connection_object.send_audio_from_mic()

payload = {
    'contentType': 'text/markdown',
    # 'contentType': 'text/srt',
    'createParagraphs': "true",
    'phrases': {
        'highlightOnlyInsightKeyPhrases': "true",
        'highlightAllKeyPhrases': "true"
    },
    'showSpeakerSeparation': "true"
}
print(connection_object.conversation.get_formatted_transcript(parameters= payload))