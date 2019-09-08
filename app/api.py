from flask import Blueprint, jsonify, request
import random
import json


api_blueprint = Blueprint('api', __name__)


WIDTH = 64
HEIGHT = 36


@api_blueprint.route('/board')
def api_board():
    board = [
        [
            ('%06x' % random.randint(0, 0xFFFFFF))
            for row in range(HEIGHT)
        ] for row in range(WIDTH)
    ]
    return json.dumps(board)
