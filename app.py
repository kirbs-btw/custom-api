from api import create_app
from apiflask import APIFlask
import os

API_TITLE='custom_api'
API_VERSION='1.0.0'

# create the app
app = APIFlask(__name__, title=API_TITLE, version=API_VERSION)

app.config['SERVERS'] = [
    {
        'description': 'Custom API',
        'url': '',
    },
    {
        'description': 'local test',
        'url': 'http://127.0.0.1:{port}',
        'variables':
        {
            'port':
            {
                'default': "5000",
                'description': 'local port to use'
            }
        }
    }
]

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0',port=int(port))
    

"""
def main():
    app = create_app()
    app.run(debug=True)

if __name__ == '__main__':
    main()
"""