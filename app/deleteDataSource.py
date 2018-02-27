from app import app
from app.dataAccess.mongoData import mongoData

from flask import abort


@app.route('/dataSource/<string:id>', methods=['DELETE'])
def delete_data_source(id):

    db = mongoData(app)
    result = db.remove_one(id)

    if result.deleted_count is 1:
        return f'deleted {id}', 202
    else:
        abort(404, f'data source with id {id} not found!')
