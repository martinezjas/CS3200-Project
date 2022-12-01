from flask import Blueprint, request, jsonify, make_response
import json
from src import db


teams = Blueprint('teams', __name__)

@betters.route('/teams', methods=['GET'])
def get_betters():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT teamName, country, city, conference, division FROM teams AS 'Team Name', CONCAT(city, ", ", country) AS Location, CONCAT(division, ", ", confernece) AS Division/Conference')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)  