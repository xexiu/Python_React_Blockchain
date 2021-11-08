import os
import random

import requests
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub
from backend.util.global_variables import CONFIG_PN, PEER, PORT, ROOT_PORT
from flask import Flask, jsonify

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain, **CONFIG_PN)


@app.route('/')
def default():
    return 'Welcome to Homepage'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_date = 'stubbed_transaction_date'
    blockchain.add_block(transaction_date)

    last_block_in_chain = blockchain.chain[-1]

    pubsub.broadcast_block(last_block_in_chain)

    return jsonify(last_block_in_chain.to_json())

# Default to port=5000 -> app.run() -> Or add a custom port -> app.run(port:5001)


if(os.environ.get(PEER) == 'True'):
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://127.0.0.1:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully synchronized the local chain')
    except Exception as e:
        print(f'\n -- Error synchronizing: {e}')


app.run(port=PORT)
