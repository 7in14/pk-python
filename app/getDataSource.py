from app import app, get_mongo
from tools import JSONEncoder
from flask import jsonify, abort
from bson.objectid import ObjectId
# todo: switch to async await ? https://github.com/xzased/pytest-async-mongodb


@app.route('/dataSource/<string:id>')
def get_dataSource(id):
    if not id:
        abort(404)

    source = get_mongo().db.dataSources.find_one_or_404(ObjectId(id))
    return JSONEncoder.JSONEncoder().encode(source)
