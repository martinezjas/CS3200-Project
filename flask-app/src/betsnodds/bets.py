from flask import Blueprint, request, jsonify, make_response
import json
from src import db

bets_blueprint = Blueprint('bets_blueprint', __name__)


@bets_blueprint.route('/', methods=['GET'])
def empty():
    return ('<h1>You are not authorized to access this page!</h1>')
