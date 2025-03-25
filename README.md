Chatbot Project

This is a simple chatbot built using Django and PyTorch. It uses a neural network to process user input and generate responses based on predefined intents.

Features

Django-based backend

PyTorch-based chatbot model

JSON-based intents for response handling

Interactive frontend with HTML, CSS, and JavaScript

Installation

1. Clone the repository:

git clone https://github.com/abhishekk1004/gnome.git
cd chatbot

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

3. Install dependencies:

pip install -r requirements.txt

4. Run Migrations:

python manage.py migrate

5. Start the server:

python manage.py runserver

Project Structure

chatbot/
│-- chatbot/ (Main Django App)
│   │-- static/
│   │   │-- chatbot.js
│   │   │-- style.css
│   │-- templates/
│   │   │-- chatbot.html
│   │-- utils/
│   │   │-- chat.py
│   │   │-- intents.json
│   │-- views.py
│-- manage.py
│-- requirements.txt
│-- README.md
│-- .gitignore

API Endpoint

POST /chatbot/: Sends a user message and receives a chatbot response.

Contributing

Feel free to fork and contribute to this project. Submit a pull request with your improvements!

License

This project is open-source and free to use.
