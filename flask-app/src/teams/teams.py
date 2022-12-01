from flask import Blueprint, request, jsonify, make_response
import json
from src import db


teams = Blueprint('teams', __name__)

@teams.route('/teams', methods=['GET'])
def get_teams():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT teamName AS 'Team Name', CONCAT(city, ", ", country) AS Location, CONCAT(conference, ", ", division) AS 'Conference, Division' FROM teams')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)  