from flask import Flask, render_template
import random

app = Flask(__name__)

services = {
"algo-surge": {
"id": 282,
"name": "algo-surge",
"git_repo": "algo_surge_service",
"cd": False,
"language": "python",
"docker": True,
"docker_url": "algo_surge_service",
"enable": True
},
"area": {
"id": 30,
"name": "area",
"git_repo": "area_service.git",
"cd": True,
"language": "ruby",
"docker": False,
"docker_url": "area_service",
"enable": True,
"owner": {
"id": 5,
"name": "Timor Wienrib",
"github_user": "timorw",
"slack_user": "",
"email": ""
}
},
"arm": {
"id": 61,
"name": "arm",
"git_repo": "arm_service.git",
"cd": False,
"language": "golang",
"docker": True,
"docker_url": "arm_service",
"enable": True
}}
@app.route('/services')
def print_services():
    return render_template('services.html', services=services)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found</h1>", 404


@app.errorhandler(505)
def server_error(e):
    return "<h1>Internal server Error</h1>", 500


if __name__ == '__main__':
    app.run(port=3000, debug=True)
