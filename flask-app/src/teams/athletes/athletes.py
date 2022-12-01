from flask import Blueprint, request, jsonify, make_response
import json
from src import db


athletes = Blueprint('athletes', __name__)

@athletes.route('/athletes', methods=['GET'])
def get_athletes():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT CONCAT(firstName, " ", lastName) AS Name, height, weight, age, teamName AS 'Team Name' FROM athletes')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)  