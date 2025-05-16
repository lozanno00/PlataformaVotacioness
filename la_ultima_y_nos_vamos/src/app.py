# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Voting Platform!"

if __name__ == '__main__':
    app.run(debug=True)