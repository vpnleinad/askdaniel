from flask import Flask, render_template, request
from dotenv import load_dotenv
import os, openai


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':

    portas = process.env.get('PORT', 8080)
    app.run(host='127.0.0.0', port=portas, debug=False)