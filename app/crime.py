from app import app
from flask import request
from flask import jsonify
import requests

# GET /raleigh/crime?query=<q> JSON
# Calls Open Data Endpoint for Raleigh and filters crimes by matching the provided query.
# Data URL to use:https://data.raleighnc.gov/Police/Daily-Police-Incidents/guyh-emm5


@app.route('/raleigh/crime')
def crime():
    query = request.args.get('query')

    r = requests.get('https://data.raleighnc.gov/resource/3bhm-we7a.json')
    json = r.json()
    return jsonify(json)
