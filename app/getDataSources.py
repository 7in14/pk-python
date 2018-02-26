from app import app, get_mongo
from app.dataAccess.mongoData import mongoData
from tools import JSONEncoder


@app.route('/dataSources')
def get_data_sources():

    db = mongoData(get_mongo())
    sources = db.get_all()
    return JSONEncoder.JSONEncoder().encode(list(sources))
