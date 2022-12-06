from flask import Blueprint, request, jsonify, make_response
import json
from src import db

athletes_blueprint = Blueprint('athletes_blueprint', __name__)


@athletes_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>How did you get here?</h1>')


@athletes_blueprint.route('/view_athletes', methods=['GET'])
def get_athletes():
    cursor = db.get_db().cursor()

    cursor.execute(
        'SELECT CONCAT(firstName, " ", lastName) AS Name, height, weight, age, teamName AS "Team Name" FROM athlete')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@athletes_blueprint.route('/view_athlete/<idNumber>')    
def get_athlete(idNumber):
    cursor = db.get_db().cursor()
    cursor2 = db.get_db().cursor()

    cursor.execute('SELECT * FROM athlete WHERE athlete_id = %s', idNumber)
    cursor2.execute('SELECT * FROM athlete_career_stats WHERE athlete_id = %s', idNumber)

    column_headers = [x[0] for x in cursor.description]
    column_headers2 = [x[0] for x in cursor2.description]

    json_data = []
    json_data2 = []

    theData = cursor.fetchall()
    theData2 = cursor2.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    for row in theData2:
        json_data2.append(dict(zip(column_headers2, row)))

    return jsonify(json_data, json_data2)