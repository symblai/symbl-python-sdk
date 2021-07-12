import symbl

payload = {
    "name": "TextAPI", #you can update the name of the conversation

    "messages": [
        {
            "duration": {"startTime": "2021-06-18T12:08:19.99Z", "endTime": "2021-06-18T12:10:20.99Z"},

            "payload": {
                "content": "Hello.  So this is a live demo that we are trying to give very we are going to show how the platform detects various insights can do transcription in real-time and also the different topics of discussions, which would be generated after the call is over, and they will be an email that will be sent to the inbox.  So that is the idea.  So I am going to do a quick conversation.  I would say where I will demonstrate all of this great catching up.  Thanks for calling good to hear.  From you.  And I would love to hear more about what you have to offer?  I will set up a time and appointment probably sometime tomorrow evening where we can go over the documents that you're providing.  I love all the plants.  I just need to discuss with my family in terms of which one will we go forward with it?  It very excited to hear from you and the discount and look forward to talking sharply.  I have a quick question though.  Is there basically website?  Where I can go to and look at all these details myself.  It will be very helpful.  Can you also share the quotation to me on email so that I can go ahead and talk about it with my other kind of folks in the family?  That's it.  Thanks a lot.  Thanks for calling good catching up.  Talk soon.",
                "contentType": "text/plain"
            },
            "from": {"name": "John", "userId": "john@example.com"}
        }
    ]
}

conversation = symbl.Text.process(payload=payload)

print(conversation.get_conversation())
print(conversation.get_messages())
#print(conversation.get_action_items())
#print(conversation.get_follow_ups())
#print(conversation.get_members())
#print(conversation.get_topics())
#print(conversation.get_questions())



