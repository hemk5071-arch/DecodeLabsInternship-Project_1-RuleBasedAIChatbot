import random
from datetime import datetime

class chatbot:
    def __init__ (self):
        self.reply = {
            "hi":[
                "Hello","Hi there!","Hey!","Hey! What's up","How do you do?"
            ],
            "hello":[
                "Hello","Hi there!","Hey!","Hey! What's up","How do you do?"
            ],
            "how are you":[
                "I'm doing great!","I'm fine","All good! How about you?","Great! Glad to see you"
            ],
            "name":[
                "My name is chatbot","I am a simple python chatbot","you can call me chatbot","This is chatbot "
            ],
            "help":[
                "You can ask me simple questions.","I can assist you to simple questions","I can help you to simple questions"
            ],
            "date":[
                ("Today's Date:" + datetime.now().strftime("%d-%m-%Y"))
            ],
            "time":[
                ("Time:"+ datetime.now().strftime("%H:%M:%S"))
            ],
            "what is ai": [
                "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence."
            ],
            "what is ml":[
                "Machine Learning is a branch of AI that allows computers to learn from data."
            ],
            "what is deep learning":[
                "Deep Learning is a type of Machine Learning that uses neural networks with many layers."
            ],
            "what is data science":[
                "Data Science is the process of extracting useful insights from data."
            ],
            "what is nlp":[
                "Natural Language Processing helps computers understand and process human language."
            ],
            "what is computer vision":[
                "Computer Vision enables computers to understand images and videos."
            ],
            "what is generative ai":[
                "Generative AI creates new content such as text, images, audio, and code."
            ],
            "what is a neural network":[
                "A Neural Network is a system inspired by the human brain that helps machines learn patterns."
            ],
            "what is python":[
                "Python is a popular programming language used in AI, Machine Learning, and web development."
            ],
            "what is chatbot":[
                "A chatbot is a software program that can communicate with users through text or voice."
            ],
            "what is cnn":[ 
                "CNN stands for Convolutional Neural Network, a deep learning model used for image recognition."
            ],
            "what is training data":[
                "Training data is the data used to teach a machine learning model."
            ],
            "what is model":[
                "A model is a program trained to make predictions or decisions from data."
            ],
            "what is automation":[
                "Automation is the use of technology to perform tasks with minimal human intervention."
            ],
            "what is robotics":[
                "Robotics is the field of designing and building intelligent machines called robots."
            ],
            "what is full stack": [
                "A Full Stack Developer works on both the frontend and backend of web applications."
            ],
            "what is frontend": [
                "Frontend development focuses on the user interface using HTML, CSS, JavaScript, and frameworks like React."
            ],
            "what is backend": [
                "Backend development handles the server, database, APIs, and business logic using technologies like Python, Node.js, Java, or PHP."
            ],
            "what is html": [
                "HTML is the standard markup language used to create web pages."
            ],
            "what is css": [
                "CSS is used to style and design web pages."
            ],
            "what is javascript": [
                "JavaScript adds interactivity and dynamic behavior to websites."
            ],
            "what is react": [
                "React is a JavaScript library for building fast and interactive user interfaces."
            ],
            "what is database": [
                "A database stores and manages application data. Popular databases include MySQL, PostgreSQL, and MongoDB."
            ],
            "what is api": [
                "An API (Application Programming Interface) allows different software applications to communicate with each other."
            ],
            "what is git": [
                "Git is a distributed version control system used to track changes in source code."
                ],
            "what is github": [
                "GitHub is a cloud platform that hosts Git repositories and helps developers collaborate on projects."
                ],
            "bye":[
                "Goodbye!","See you later!","Have a nice day!","Bye!,Have a great day!"
            ]
        }
    
    def get_reply(self,user_input):
        user_input = user_input.lower()
        
        for ans in self.reply:
            if ans in user_input:
                return random.choice(self.reply[ans])
            
        return "Sorry, I don't understand that."
            
bot = chatbot()