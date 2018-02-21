from app import app
from flask import request, jsonify
import requests

# GET /raleigh/crime?query=<q> JSON
# Calls Open Data Endpoint for Raleigh and filters crimes by matching the provided query.
# Data URL to use:https://data.raleighnc.gov/Police/Daily-Police-Incidents/guyh-emm5


@app.route('/raleigh/crime')
def crime():
    query = request.args.get('query')

    r = requests.get('https://data.raleighnc.gov/resource/3bhm-we7a.json')
    json = r.json()

    # filter list
    filtered = list(filterbyvalue(json, query))

    return jsonify(filtered)


def filterbyvalue(seq, value):
    for el in seq:
        if not value or value in el['lcr_desc']:
            if 'location' in el:
                del el['location']
            if 'inc_no' in el:
                del el['inc_no']
            yield el
