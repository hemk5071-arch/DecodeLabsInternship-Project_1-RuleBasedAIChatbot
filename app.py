from flask import Flask, render_template, request, jsonify
from RuleBasedChatbot import bot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbot-index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = bot.get_reply(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)