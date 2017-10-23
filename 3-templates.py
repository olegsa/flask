from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/user/<path:user>')
def hello_user(user):
    return render_template('user.html', user=user, color=random_color())


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found</h1>", 404


@app.errorhandler(500)
def server_error(e):
    return "<h1>My Internal server Error</h1>", 500


def random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


if __name__ == '__main__':
    app.run(port=3000, debug=True)
