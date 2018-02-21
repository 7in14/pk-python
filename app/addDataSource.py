from app import app
from flask import jsonify, abort, request


@app.route('/dataSource', methods=['PUT'])
def add_dataSource():

    if not request.json or not 'url' in request.json or not 'name' in request.json:
        abort(400)
    dataSource = {
        'name': request.json['name'],
        'url': request.json['url']
    }
    return jsonify(dataSource), 201
