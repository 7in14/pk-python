from app import app, mongo, JSONEncoder
from flask import jsonify, abort
from bson.objectid import ObjectId


@app.route('/dataSource/<string:id>')
def getDataSource(id):
    if not id:
        abort(404)
    print('Looking for dataSource with id:' + id)
    source = mongo.db.dataSources.find_one_or_404(ObjectId(id))

    return JSONEncoder.JSONEncoder().encode(source)
