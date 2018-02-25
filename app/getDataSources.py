from app import app, get_mongo
from tools import JSONEncoder


@app.route('/dataSources')
def get_data_sources():

    sources = get_mongo().db.dataSources.find({})
    return JSONEncoder.JSONEncoder().encode(list(sources))
