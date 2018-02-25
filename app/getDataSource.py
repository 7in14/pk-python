from app import app, get_Mongo
from tools import JSONEncoder
from flask import jsonify, abort
from bson.objectid import ObjectId
# todo: switch to async await ? https://github.com/xzased/pytest-async-mongodb


@app.route('/dataSource/<string:id>')
def get_DataSource(id):
    if not id:
        abort(404)

    source = get_Mongo().db.dataSources.find_one_or_404(ObjectId(id))
    return JSONEncoder.JSONEncoder().encode(source)
