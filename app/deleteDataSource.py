from app import app
from flask import jsonify,abort

@app.route('/dataSource/<string:id>', methods=['DELETE'])

def delete_dataSource(id):
    if not id or id == "1":
        abort(404)
    return jsonify({'task deleted': id})
