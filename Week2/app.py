from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello():
    return "Hello Everyone"

app.run(port=8080,debug=True)
