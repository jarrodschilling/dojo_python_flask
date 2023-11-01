from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/play/<int:num>/<string:color_test>')
def play(num, color_test):
    return render_template('play.html', num=num, color_test=color_test)


if __name__=="__main__":
    app.run(debug=True)