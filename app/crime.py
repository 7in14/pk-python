from app import app
from flask import request

# GET /raleigh/crime?query=<q> JSON
# Calls Open Data Endpoint for Raleigh and filters crimes by matching the provided query.Data URL to use:https://data.raleighnc.gov/Police/Daily-Police-Incidents/guyh-emm5

@app.route('/raleigh/crime')

def crime():
    query = request.args.get('query')
    return 'you requested ' + query
