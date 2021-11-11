import os
import random

from backend.app.route import Route
from backend.util.global_variables import PEER, PORT, SEED_DATA

route = Route(__name__)


@route.app.route('/')
def default():
    return route.default()


@route.app.route('/blockchain')
def route_blockchain():
    return route.route_blockchain()


@route.app.route('/blockchain/mine')
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
# Default to port=5000 -> app.run() -> Or add a custom port -> app.run(port:5001)


if(os.environ.get(PEER) == 'True'):
    PORT = random.randint(5001, 6000)
    route.get_new_chain()

if os.environ.get(SEED_DATA) == 'True':
    route.seed_data()


route.app.run(port=PORT)
