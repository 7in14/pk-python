from app import app
from app.dataAccess.mongoData import mongoData

from flask import abort, request
from tools import JSONEncoder
from bson.objectid import ObjectId


@app.route('/dataSource', methods=['PUT'])
def add_data_source():

    if not request.json or not 'url' in request.json or not 'name' in request.json:
        abort(400, f'provided json payload was not correct: {request.json}')
    dataSource = {
        'name': request.json['name'],
        'url': request.json['url']
    }

    _id = request.json.get('_id', None)

    if _id is not None:
        dataSource['_id'] = ObjectId(_id)

    db = mongoData(app)
    result = db.add_one(dataSource)

    return JSONEncoder.JSONEncoder().encode(result.inserted_id), 201
