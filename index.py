from flask import Flask, jsonify, request, json
from markupsafe import escape

app = Flask(__name__) # seems to be a __constant__ which is not defined here (__BLBLA__)
responses = ["Hello","Goodbye", "Tschuess", "Auf wiedersehen"] #static list
@app.route("/") # index/main endpoint/route
def hello_world():
    return "<h1>Hello, Maria!</h1>"

@app.route("/messages") # static endpoint/route
def messages():
    return jsonify(responses) # transforms into json format for valid htttp response

@app.route('/messages/<int:messege>') # get a vairable in the path of the request url
def show_user_profile(messege):
    # show the user profile for that user
    return responses[messege]

# you can have 2 routes (/chat) with the same PATH but different METHODS (GET, POST)
@app.route('/chat')
def chatGET():
    return "chatGET" # simple RESPONDES with "chatGET"

# request the follow ing route/endpoint with this command:
# curl -X POST -d 'message=Hi' localhost:5000/chat
@app.route('/chat', methods = ['POST'])
def chat():
    data = request.get_json(force=True)
    print(data["email"]) # prints message=Hi from the request
    print(data["password"]) # prints message=Hi from the request
    # TODO get specific message (Hi) from request body
    return "chatPOST" # simple RESPONDES with "test"

app.run() # run the app as a final statement
