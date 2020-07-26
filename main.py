import logging
import requests
import pandas as pd
from flask import Flask
from flask_cors import cross_origin
from flask import make_response

app = Flask(__name__)


@app.route("/")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello_world(request):
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        correlation = df.corr(method='pearson')
        resp = make_response(correlation.to_csv())
        resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp
    return "Ok"
