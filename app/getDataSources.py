from app import app
from flask import jsonify

data = [
    {
        'name': u'US States',
        'url': u'http://services.groupkt.com/state/get/USA/all'
    },
    {
        'name': u'JSON placeholder',
        'url': u'https://jsonplaceholder.typicode.com/users',
    }
]

@app.route('/dataSources')

def get_dataSources():
    return jsonify(data)
