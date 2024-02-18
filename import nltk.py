import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Define pairs of patterns and responses
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']],
    ['what is your name?', ['You can call me Chatbot.', 'My name is Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Start chatting
print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ").lower()
    if user_input == 'quit':
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
