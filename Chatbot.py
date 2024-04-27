chat_response = ["Hello my name Sipho The new chatbot how may i assist you? ","You shift starts at 9:00 am","I Have no sex or what you might call gender","Iam 10days old","Iam an AI chatbot i dont have feeling like humans do","Iam an AI Chatbot i was built BY Nator to help you with any question you have","do you have any question i amy answer? ","sorry i didnt get the message please retype your question (Watch Your Spelling!)"]

chat_data = ["Hello","When does my shift start","How are you","What are you","How old are you","are you male or female"]
chat = True
def Chat(chat):
    while chat == True:
        chat = input(chat_response[0])
        if chat == chat_data[0].lower() or chat == chat_data[0].upper():
            print("\n" + chat_response[0])
        elif chat == chat_data[1].lower() or chat == chat_data[1].upper():
            print("\n" + chat_response[1])
            break
        elif chat == chat_data[2].lower() or chat == chat_data[2].upper():
            print("\n" + chat_response[4])
            break
        elif chat == chat_data[3].lower() or chat == chat_data[3].upper():
            print("\n" + chat_response[5])
            break
        elif chat == chat_data[4].lower() or chat == chat_data[4].upper():
            print("\n" + chat_response[3])
            break
        elif chat == chat_data[5].lower() or chat == chat_data[5].upper():
            print("\n" + chat_response[2])
            break
        else:
            print(chat_response[7])
            break



Chat(chat)

