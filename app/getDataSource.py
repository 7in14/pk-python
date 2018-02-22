from app import app, getMongo
from tools import JSONEncoder
from flask import jsonify, abort
from bson.objectid import ObjectId
# todo: switch to async await ? https://github.com/xzased/pytest-async-mongodb


@app.route('/dataSource/<string:id>')
def getDataSource(id):
    if not id:
        abort(404)
    print(JSONEncoder)
    print('Looking for dataSource with id:' + id)
    source = getMongo().db.dataSources.find_one_or_404(ObjectId(id))

    return JSONEncoder.JSONEncoder().encode(source)
