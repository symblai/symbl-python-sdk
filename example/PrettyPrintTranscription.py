### Sample Code to pretty print all the messages

import symbl

# API call to process audio file
conversation = symbl.Audio.process_file(file_path="D:\Hani\Symbl\Internship\Material\sample_audio_file.wav")

# Function to extract a key from the json array response
extract_text = lambda responses : [response.text for response in responses]

# Function to print each message of a text_array on a new line
pretty_print = lambda text_array : [print(text) for text in text_array]

# Fetching actual transcripts using the conversationId
response = conversation.get_messages()

# pretty printing transcripts (every message on a new line) 
pretty_print(extract_text(response.messages))