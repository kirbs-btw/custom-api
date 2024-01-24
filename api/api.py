from flask import Blueprint, render_template
from flask import request

api = Blueprint('api', __name__)

@api.route('/api/ping')
def ping():
    package = request.args['package']
    return {
        "message": "package recieved",
        "package": package,
            }

@api.route('/api/status')
def status():
    expl_json = {
        "message" : "active"
    }

    return expl_json