from flask import Blueprint, request, jsonify, make_response
import json
from src import db

bets = Blueprint('bets', __name__)