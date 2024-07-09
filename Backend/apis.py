#!/usr/bin/python3
"""Flask app for CRUD operations on Hospital, Patient, and PatientHealthInfo models"""
from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS
from models import storage
from models.product import Product
from models.store import Store
from models.audit import Audit

import logging
import pandas as pd
import joblib

# Load the trained model from the file
# classifier_rf = joblib.load('model.pkl')


app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False


@app.route('/api/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app.route('/api/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = ["Product", "Store", "Audit"]
    names = ["products", "stores", "audits"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])
    return jsonify(num_objs)

@app.route('/api/stores', methods=['GET'])
def get_stores():
    try:
        stores = storage.all(Store).values()
        return jsonify([store.to_dict() for store in stores])
    finally:
        storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
