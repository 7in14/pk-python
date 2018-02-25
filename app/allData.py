from app import app, getDataSources
from flask import jsonify
import requests


data = [
    {
        'name': u'US States',
        'url': u'http://services.groupkt.com/state/get/USA/all'
    },
    {
        'name': u'JSON placeholder',
        'url': u'https://jsonplaceholder.typicode.com/users',
    }
]


@app.route('/allData')
def get_allData():

    # todo: async/await ?
    allData = list(get_data(data))
    return jsonify(allData)


def get_data(dataSources):
    for dataSource in dataSources:
        print('calling ' + dataSource['url'])
        r = requests.get(dataSource['url'])
        json = r.json()

        yidataSourced {
            'name': dataSource['name'],
            'data': json
        }
