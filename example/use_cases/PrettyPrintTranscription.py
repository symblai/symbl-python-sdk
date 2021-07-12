# Sample Code to pretty print all the messages
# Using this example you can extract the different keys from response object returned by conversation object

import symbl

# API call to process audio file
conversation_object = symbl.Audio.process_file(file_path="<file_path>")

# Function to extract a key from the json array response
extract_text = lambda responses : [response.text for response in responses]

# Function to print each message of a text_array on a new line
pretty_print = lambda text_array : [print(text) for text in text_array]

# Fetching actual transcripts using the conversationId
response = conversation_object.get_messages()

# pretty printing transcripts (every message on a new line) 
pretty_print(extract_text(response.messages))