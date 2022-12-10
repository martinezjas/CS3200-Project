from flask import Blueprint, request, jsonify, make_response
import json
from src import db

betters_blueprint = Blueprint('betters_blueprint', __name__)


@betters_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>How did you get here?</h1>')


@betters_blueprint.route('/view_betters', methods=['GET'])
def get_betters():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM betters')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@betters_blueprint.route('/add_better', methods=['POST'])
def add_better():
    cursor = db.get_db().cursor()
    currencyTotal = request.form['currencyTotal']
    query = f'INSERT INTO betters (currencyTotal) VALUES (\"{currencyTotal}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "New Better Created!"


