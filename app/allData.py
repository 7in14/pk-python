from app import app, get_mongo
from app.dataAccess.mongoData import mongoData

from flask import jsonify
import requests


@app.route('/allData')
def get_all_data():

    # todo: async/await ?
    # todo: use ray?
    db = mongoData(get_mongo())
    data = db.get_all()
    allData = list(get_data(data))
    return jsonify(allData)


def get_data(dataSources):
    for dataSource in dataSources:
        print('calling ' + dataSource['url'])
        r = requests.get(dataSource['url'])
        json = r.json()

        yield {
            'name': dataSource['name'],
            'data': json
        }
