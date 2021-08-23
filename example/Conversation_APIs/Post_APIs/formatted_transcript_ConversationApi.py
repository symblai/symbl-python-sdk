import symbl
#to test API using  ConversationApi class

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
conversation_id = "1234567890" #update with your conversation id
print(symbl.Conversations.get_formatted_transcript(parameters=payload,conversation_id=conversation_id))
