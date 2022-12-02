from flask import Blueprint, request, jsonify, make_response
import json
from src import db

coaches_blueprint = Blueprint('coaches_blueprint', __name__)


@coaches_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>How did you get here?</h1>')


@coaches_blueprint.route('/coaches', methods=['GET'])
def get_coaches():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT CONCAT(firstName, " ", lastName) AS Name, teamName AS "Team Name" FROM coaches')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
