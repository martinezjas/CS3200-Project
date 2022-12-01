from flask import Blueprint, request, jsonify, make_response
import json
from src import db


betters = Blueprint('betters', __name__)

@betters.route('/betters', methods=['GET'])
def get_betters():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM betters')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)    