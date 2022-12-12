from flask import Blueprint, request, jsonify, make_response
import json
from src import db

games_blueprint = Blueprint('games_blueprint', __name__)


@games_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>How did you get here?</h1>')


@games_blueprint.route('/view_games', methods=['GET'])
def get_games():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT gameStatus AS "Game Status", homeTeam AS "Home Team", awayTeam AS "Away Team", CONCAT(homeResult, "-", awayResult) AS "Home-Away", finalScore AS "Final Score", weather AS Weather FROM game')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

#get specific game
@games_blueprint.route('/view_games/<idNumber>')    
def get_athlete(idNumber):
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * game WHERE game_id = %s', idNumber)

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

#get home vs away
@games_blueprint.route('/view_HvA_games')    
def get_gamesHvA():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT CONCAT(homeTeam, " V. ", awayTeam) AS "HvA", calculated_favored_team_ml, calculated_underdog_team_ml, calcuated_underdog_total, calculated_favored_total, calculated_favored_spread, caclulated_underdog_spread, oddsID FROM game JOIN odds ON game.oddsID = odds.odds_ID')

    column_headers = [x[0] for x in cursor.description]

    json_data = []

    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
