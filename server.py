import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return request.json

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
