import random
import emoji
successful_interactions = 0

user_needs = ["get information", "ask a question", "request assistance"]

chatbot_personality = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "farewell": ["Goodbye!", "Bye!", "See you later!"],
    "positive": ["Great", "Awesome", "Fantastic"],
    "negative": ["I'm sorry.", "Apologies.", "My apologies."],
    "unknown": ["I'm not sure.", "I don't know.", "I can't answer that."]
}

chatbot_flow = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you today?"],
    "farewell": ["Goodbye!", "Bye!", "See you later!"],
    "positive": ["I'm glad you're satisfied!", "I'm happy to help!", "You're welcome!"],
    "help":["I'm happy to help you"],
    "code":["Sorry,but I'm not trained to help you with that"],
    "negative": ["I'm sorry to hear that.", "I'll do my best to improve.", "I apologize for any inconvenience."],
    "unknown": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure how to respond."],
    "Info": ["A friendly chatbot is a conversational AI program that is designed to interact with users in a pleasant and helpful manner.It is programmed to understand and respond to user queries, provide information, and assist with tasks in a friendly and approachable way.","Ask any Question you want."]
}


def get_user_input():
    user_input = input("User: ")
    return user_input.lower()


def generate_chatbot_response(user_input):
    chatbot_response = ""
    user_input = user_input.lower()

    
    if any(need in user_input for need in user_needs):
        chatbot_response = random.choice(chatbot_flow["Info"])
        global successful_interactions
        successful_interactions += 1
    elif "hi" in user_input or "hello" in user_input:
        chatbot_response = random.choice(chatbot_flow["greeting"])
    elif "Great" in user_input or "Awesome" in user_input:
        chatbot_response = random.choice(chatbot_flow["positive"])
    elif "help" in user_input or "ask" in user_input:
        chatbot_response = random.choice(chatbot_flow["help"])
    elif "code" in user_input or "program" in user_input:
        chatbot_response = random.choice(chatbot_flow["code"])
    elif "bye" in user_input or "goodbye" in user_input:
        chatbot_response = random.choice(chatbot_flow["farewell"])
    else:
        chatbot_response = random.choice(chatbot_flow["positive"])
    return chatbot_response


def start_chatbot():
    
    while True:
        user_input = get_user_input()
        if user_input == "exit":
            break
        chatbot_response = generate_chatbot_response(user_input)
        print("Chatbot: " + chatbot_response)


print("Welcome to Chatbot!")
print("Chatbot: " + "How may i assist you today ", emoji.emojize(":grinning_face_with_big_eyes:"))
start_chatbot()


print("Successful Interactions: " + str(successful_interactions))