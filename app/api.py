from flask import Blueprint, jsonify, request, abort
import os
import random
import json
import redis

api_blueprint = Blueprint('api', __name__)
r = redis.from_url(os.environ.get('REDIS_URL', 'redis://localhost:6379'))


WIDTH = 64
HEIGHT = 36

if not r.llen('board'):
    for index in range(WIDTH * HEIGHT):
        r.lpush('board', *[('%06x' % 0x000000) for row in range(WIDTH * HEIGHT)])


def random_board():
    board = [
        [
            ('%06x' % random.randint(0, 0xFFFFFF))
            for row in range(HEIGHT)
        ] for row in range(WIDTH)
    ]


def get_index(x, y):
    return WIDTH * x + y

def get_position(index):
    return index // WIDTH, index % WIDTH


@api_blueprint.route('/board')
def api_board():
    board = json.dumps([color.decode() for color in r.lrange('board', 0, WIDTH * HEIGHT)])
    return board


@api_blueprint.route('/set/<x>/<y>/<color>', methods=['POST'])
def api_set(x, y, color):
    x = int(x)
    y = int(y)
    if x >= WIDTH or y >= HEIGHT:
        abort(401)
    r.lset('board', get_index(x, y), color)
    return 'OK', 200
