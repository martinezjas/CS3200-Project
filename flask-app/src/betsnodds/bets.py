from flask import Blueprint, request, jsonify, make_response
import json
from src import db

bets_blueprint = Blueprint('bets_blueprint', __name__)


@bets_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>You are not authorized to access this page!</h1>')

@bets_blueprint.route('/enter_bet', methods=['POST'])
def make_bet():
    cursor = db.get_db().cursor()
    better_id = request.form['better_id']
    fml = request.form['fml']
    uml = request.form['uml']
    fbet = request.form['fbet']
    ubet = request.form['ubet']
    fspread = request.form['fspread']
    uspread = request.form['uspread']
    query = f'INSERT INTO bet(better_id,favored_moneyline,underdog_moneyline,favored_team_bet_amount,' \
            f'underdog_team_bet_amount,favored_team_spread_amount,underdog_team_spread_amount) ' \
            f'VALUES(\"{better_id}\",\"{fml}\",\"{uml}\",\"{fbet}\",\"{ubet}\",\"{fspread}\",\"{uspread}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Your bet has been placed!"

@bets_blueprint.route('/getbet', methods=['GET'])
def see_bet():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM bet')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)