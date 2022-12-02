from flask import Blueprint, request, jsonify, make_response
import json
from src import db


games = Blueprint('games', __name__)

@games.route('/games', methods=['GET'])
def get_games():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT gameStatus AS 'Game Status', homeTeam AS 'Home Team', awayTeam AS 'Away Team', CONCAT(homeResult, "-", awayResult) AS 'Home-Away', finalScore AS 'Final Score', weather AS 'Weather', FROM game')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data) 