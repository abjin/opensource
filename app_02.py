from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, Flask!</h1>'


@app.route('/about')
def about():
    return f'<h1>안녕하세요, about 페이지입니다!</h1>'


@app.route('/hello/<name>')
def hello(name):
    return f'<h1>안녕하세요, {name}님!</h1>'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=10005)
