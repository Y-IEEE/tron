from flask import Blueprint, jsonify, request
import random


api_blueprint = Blueprint('api', __name__)


HEIGHT = 36
WIDTH = 64


@api_blueprint.route('/board')
def api_board():
    board = [
        [
            ('%06x' % random.randint(0, 0xFFFFFF))
            for row in range(WIDTH)
        ] for row in range(HEIGHT)
    ]
    return str(board)
