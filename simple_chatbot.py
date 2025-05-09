# Simple chatbot

responses = {
    "Hello": "Hi! How can I assist you?",
    "How are you?": "I'm an AI, so I don't have feelings, but I'm here to help you!",
    "What's your name?": "I am a chatbot. I don't have a name, but it's nice to meet you."
}

def get_response(user_input):
    return responses.get(user_input, "Sorry, I didn't understand that. Feel free to ask something else.")

def chatbot():
    print("Welcome to the chatbot! (Type 'exit' to quit.)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()