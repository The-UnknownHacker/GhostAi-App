from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from google.generativeai.types.safety_types import HarmBlockThreshold
from convo import convo
from api_key import enc_api_key

genai.configure(api_key=enc_api_key)
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/privacy')
def Privacy():
    return render_template('Privacy.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form.get('user_input')
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    response = convo.send_message(user_input).text
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5001)
