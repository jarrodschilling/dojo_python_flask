from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', num1=4, num2=4)

@app.route('/<int:num1>')
def x_(num1):
    num1 = num1 / 2
    num1 = int(num1)
    return render_template('index.html', num1=num1, num2=4)

@app.route('/<int:num1>/<int:num2>')
def y_(num1, num2):
    num1 = num1 / 2
    num1 = int(num1)

    num2 = num2 / 2
    num2 = int(num2)
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def colors(num1, num2, color1, color2):
    num1 = num1 / 2
    num1 = int(num1)

    num2 = num2 / 2
    num2 = int(num2)
    return render_template('index.html', num1=num1, num2=num2, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)