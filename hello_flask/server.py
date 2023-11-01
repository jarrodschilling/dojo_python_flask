from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', phrase='hello', times=5)

@app.route('/success')
def success():
    return 'SUCCESS'

@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return render_template('hello.html', name=name, num=num)


if __name__=="__main__":
    app.run(debug=True)