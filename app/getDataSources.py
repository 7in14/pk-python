from app import app
from app.dataAccess.mongoData import mongoData
from tools import JSONEncoder


@app.route('/dataSources')
def get_data_sources():

    db = mongoData(app)
    sources = db.get_all()
    return JSONEncoder.JSONEncoder().encode(list(sources))
