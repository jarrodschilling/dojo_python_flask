from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:x>')
def say(x):
    return f"Hi {x}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return num*word

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."


if __name__=="__main__":
    app.run(debug=True)