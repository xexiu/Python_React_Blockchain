import os
import random

from backend.app.route import Route
from backend.util.global_variables import PEER, PORT

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

# Default to port=5000 -> app.run() -> Or add a custom port -> app.run(port:5001)

if(os.environ.get(PEER) == 'True'):
    PORT = random.randint(5001, 6000)
    route.get_new_chain()

route.app.run(port=PORT)
