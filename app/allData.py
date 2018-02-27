from app import app
from app.dataAccess.mongoData import mongoData

from flask import jsonify
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError
import requests


@app.route('/allData')
def get_all_data():

    # todo: async/await ?
    # todo: use ray?
    db = mongoData(app)
    data = db.get_all()
    allData = list(get_data(data))
    return jsonify(allData)


def get_data(dataSources):
    for dataSource in dataSources:
        print('calling ' + dataSource['url'])
        try:
            r = requests.get(dataSource['url'])
            json = r.json()
        except JSONDecodeError:
            json = f"could not json parse response from {dataSource['url']}"
        except ConnectionError:
            json = f"could not connect to remote server: {dataSource['url']}"

        yield {
            'name': dataSource['name'],
            'data': json
        }
