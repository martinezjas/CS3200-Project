from flask import Blueprint, request, jsonify, make_response
import json
from src import db

bets = Blueprint('bets', __name__)

@bets.route('/make_bet', methods=['POST'])
def post_make_bet():
    better_id = request.form['better_id']
    f_ml = request.form['f_ml']
    u_ml = request.form['u_ml']
    f_bet_amt = request.form['f_bet_amt']
    u_bet_amt = request.form['u_bet_amt']
    f_spd_amt = request.form['f_spd_amt']
    u_spd_amt = request.form['u_spd_amt']
    # do something here

@bets.route('/make_bet')
def get_make_bet():
