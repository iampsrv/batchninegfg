from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    api_key = os.environ.get('API_KEY')
    if api_key:
        return f'Hello! Your API key is: {api_key}'
    else:
        return 'API key not found.'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
