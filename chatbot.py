from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I'm your friendly chatbot!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return chatbot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
