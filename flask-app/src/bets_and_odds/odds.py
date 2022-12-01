from flask import Blueprint, request, jsonify, make_response
import json
from src import db


odds = Blueprint('odds', __name__)

@odds.route('/odds', methods=['GET'])
def get_odds():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM odds')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data) 