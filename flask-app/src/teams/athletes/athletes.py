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
