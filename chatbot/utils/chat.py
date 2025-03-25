# import nltk
# import json
# import numpy as np
# from tensorflow.keras.models import load_model
# from .nltk_utils import bag_of_words, tokenize

# # Load intents file & trained model
# intents = json.loads(open("chat/utils/intents.json").read())
# model = load_model("chat/utils/chatbot_model.h5")

# def chatbot_response(msg):
#     # Process user input
#     sentence = tokenize(msg)
#     bow = bag_of_words(sentence)
#     res = model.predict(np.array([bow]))[0]
    
#     if max(res) < 0.5:
#         return "I didn't understand. Can you rephrase?"
    
#     return intents['responses'][np.argmax(res)]


# import torch
# import torch.nn as nn
# import torch.optim as optim
# import random

# # Simple neural network model
# class ChatbotModel(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(ChatbotModel, self).__init__()
#         self.l1 = nn.Linear(input_size, hidden_size)
#         self.l2 = nn.Linear(hidden_size, output_size)
#         self.relu = nn.ReLU()

#     def forward(self, x):
#         x = self.relu(self.l1(x))
#         x = self.l2(x)
#         return x

# # Dummy trained model (Replace with real training logic if needed)
# def chatbot_response(user_input):
#     responses = [
#         "Hello! How can I assist you?",
#         "I'm here to help!",
#         "Tell me more about your problem.",
#         "That sounds interesting! Can you elaborate?",
#         "I'm not sure I understand. Can you rephrase?",
#     ]
#     return random.choice(responses)


# import json
# import random
# import torch
# import torch.nn as nn
# import torch.optim as optim
# from .nltk_utils import bag_of_words, tokenize

# # Load intents
# with open("chatbot/utils/intents.json", "r", encoding="utf-8") as f:
#     intents = json.load(f)

# # Define a simple PyTorch chatbot model
# class ChatbotModel(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(ChatbotModel, self).__init__()
#         self.l1 = nn.Linear(input_size, hidden_size)
#         self.l2 = nn.Linear(hidden_size, output_size)
#         self.relu = nn.ReLU()

#     def forward(self, x):
#         x = self.relu(self.l1(x))
#         x = self.l2(x)
#         return x

# # Dummy chatbot response function (replace with actual ML model later)
# def chatbot_response(msg):
#     sentence = tokenize(msg)  # Tokenize user input
#     bow = bag_of_words(sentence)  # Convert to bag-of-words format
#     response_list = []

#     for intent in intents["intents"]:
#         for pattern in intent["patterns"]:
#             if pattern.lower() in msg.lower():
#                 response_list = intent["responses"]

#     if response_list:
#         return random.choice(response_list)
    
#     return "I didn't understand. Can you rephrase?"

import json
import random
import torch
import torch.nn as nn
import torch.optim as optim
from .nltk_utils import bag_of_words, tokenize

# Load intents
with open("chatbot/utils/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# Define a simple PyTorch chatbot model
class ChatbotModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ChatbotModel, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.l1(x))
        x = self.l2(x)
        return x

# Dummy chatbot response function (replace with actual ML model later)
def chatbot_response(msg):
    sentence = tokenize(msg)  # Tokenize user input

    # 🔥 Fix: Ensure 'bag_of_words' receives the correct 'words' parameter
    vocabulary = []  # Replace with your actual vocabulary list
    bow = bag_of_words(sentence, vocabulary)  # Correct usage

    response_list = []

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in msg.lower():
                response_list = intent["responses"]

    if response_list:
        return random.choice(response_list)
    
    return "I didn't understand. Can you rephrase?"
