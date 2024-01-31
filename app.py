from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return "<li class=text-3xl font-bold> test </li>"

if __name__ == '__main__':
    app.run(debug=True)