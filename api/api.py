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

@api.push('/api/app')
def run():
    data = request.json
    
    # doing something with the pushed data
     
    return {
        "code" : 200,
        "status" : "success",
        "message" : "worked with the data"
    }
    
    
    
    