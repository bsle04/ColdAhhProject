from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define the function to be called
def my_python_function():
    return "Hello from Python!"

# Create an endpoint for the button click
@app.route('/call_function', methods=['GET'])
def call_function():
    result = my_python_function()
    return jsonify({"message": result})

# unfinished
# @app.route('/chat', methods=['GET'])
# def chat():
#     result = ask_chat(content)

if __name__ == "__main__":
    app.run(debug=True)

