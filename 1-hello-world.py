from flask import Flask

app = Flask(__name__)

page = '''
<!doctype html>
<head>
  <title>Hello Flask</title>
<body>
    <h1>Hello Flask</h1>
    <img src='static/flask.jpg' width="20%" height="20%">
</body>
</html>
'''

@app.route('/')
@app.route('/get')
def main():
    return 'Hello World'


@app.route('/index')
def index():
    return page


if __name__ == '__main__':
    app.run(port=3000, debug=True)