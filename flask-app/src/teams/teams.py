from flask import Blueprint, request, jsonify, make_response
import json
from src import db

teams_blueprint = Blueprint('teams_blueprint', __name__)


@teams_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>How did you get here?</h1>')


@teams_blueprint.route('/view_teams', methods=['GET'])
def get_teams():
    cursor = db.get_db().cursor()

    cursor.execute(
        'SELECT teamName AS "Team", CONCAT(city, ", ", country) AS Location, CONCAT(conference, ", ", division) AS "Conference, Division" FROM team')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

#specific team route
@teams_blueprint.route('/view_team/<teamName>')    
def get_athlete(teamName):
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM team WHERE teamName = %s', teamName)

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
