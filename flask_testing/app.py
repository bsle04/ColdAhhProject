from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import os
from openai import OpenAI
from utility import Wrapper

wrapper = Wrapper()
app = Flask(__name__)
CORS(app)

# Serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Test function
def my_python_function():
    return "Hello from Python!"

# Create an endpoint for the button click
@app.route('/call_function', methods=['GET'])
def call_function():
    result = my_python_function()
    return jsonify({"message": result})

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    data = request.get_json()
    content = data.get('text', '')
    response = wrapper.ask_chat(content)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

