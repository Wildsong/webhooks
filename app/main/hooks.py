import os
import json
from flask import Flask, request
from . import main

filename = "/srv/requests.json"

@main.route('/arcgis', methods=['POST','GET'])
def arcgis():
    if request.method =='GET':
        req = request.values
        return '<h1>ArcGIS spoke.</h1>' + str(req)
    if request.method =='POST':
        req = request.get_json()
        append_write = 'w'  # make a new file if not
        if os.path.exists(filename):
            append_write = 'a'  # append if already exists
        with open(filename, append_write) as fp:
            fp.write(str(json.dumps(req)))
            fp.write("\n")
        return '{"success":"true"}'

