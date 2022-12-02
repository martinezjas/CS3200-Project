from flask import Blueprint, request, jsonify, make_response
import json
from src import db

schedules_blueprint = Blueprint('schedules_blueprint', __name__)


@schedules_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>How did you get here?</h1>')


@schedules_blueprint.route('/view_schedules', methods=['GET'])
def get_games():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM schedule')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
