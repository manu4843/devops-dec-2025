from flask import Flask
app =Flask(__name__)
@app.route('/')
def home():
    return "Hello This Is  My 1st Application"
app.run(host='0.0.0.0',port=5000)