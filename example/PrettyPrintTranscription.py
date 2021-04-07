### Sample Code to pretty print all the messages

import symbl

# Initialize with credentials
symbl.init(app_id="", app_secret="")

# API call to process audio file
conversation_id = symbl.async_api.submit_audio(file_path=file_path)

# Function to extract a key from the json array response
extract_text = lambda responses : [response.text for response in responses]

# Function to print each message of a text_array on a new line
pretty_print = lambda text_array : [print(text) for text in text_array]

# Fetching actual transcripts using the conversationId
response = symbl.conversations_api.get_messages(conversation_id=conversation_id)

# pretty printing transcripts (every message on a new line) 
pretty_print(extract_text(response.messages))