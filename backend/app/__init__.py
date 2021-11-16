import os
import random

import flask
from backend.app.route import Route
from backend.util.global_variables import PEER, PORT, SEED_DATA
from flask_cors import CORS

api_v2_cors_config = {
    "origins": ["http://localhost:3000"],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization", "Content-Type", "Access-Control-Allow-Origin"]
}

route = Route(__name__)
CORS(route.app, resources={r"/*": api_v2_cors_config})


@route.app.route('/', methods=['GET'])
def default():
    return route.default()


@route.app.route('/blockchain', methods=['GET'])
def route_blockchain():
    return route.route_blockchain()


@route.app.route('/blockchain/page', methods=['GET'])
def route_blockchain_page():
    return route.route_blockchain_page()


@route.app.route('/blockchain/length', methods=['GET'])
def route_blockchain_length():
    return route.route_blockchain_length()


@route.app.route('/blockchain/mine', methods=['GET'])
def route_blockchain_mine():
    return route.route_blockchain_mine()


@route.app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    return route.route_wallet_transact()


@route.app.route('/wallet/info', methods=['GET'])
def route_wallet_info():
    return route.route_wallet_info()


@route.app.route('/jokes/random_joke', methods=['GET'])
def route_random_jokes():
    return route.route_random_jokes()


@route.app.route('/known-addresses', methods=['GET'])
def route_known_addresses():
    return route.route_known_addresses()


@route.app.route('/transactions', methods=['GET'])
def route_transactions():
    return route.route_transactions()


# Default to port=5000 -> app.run() -> Or add a custom port -> app.run(port:5001)


if(os.environ.get(PEER) == 'True'):
    PORT = random.randint(5001, 6000)
    route.get_new_chain()

if os.environ.get(SEED_DATA) == 'True':
    route.seed_data()

route.app.run(port=PORT)
