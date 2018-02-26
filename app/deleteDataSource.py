from app import app, get_mongo
from flask import jsonify, abort
from bson.objectid import ObjectId


@app.route('/dataSource/<string:id>', methods=['DELETE'])
def delete_data_source(id):

    result = get_mongo().db.dataSources.delete_one({'_id': ObjectId(id)})

    if result.deleted_count is 1:
        return f'deleted {id}', 202
    else:
        abort(404, f'data source with id {id} not found!')
