import os
import random

import requests
from backend.blockchain.blockchain import Blockchain
from backend.pubsub.pubsub import PubSub
from backend.util.global_variables import CONFIG_PN, PEER, PORT, ROOT_PORT
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.wallet import Wallet
from flask import Flask, jsonify, request

app = Flask(__name__)
blockchain = Blockchain()
wallet = Wallet()
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool, **CONFIG_PN)


@app.route('/')
def default():
    return 'Welcome to Homepage'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    blockchain.add_block(transaction_pool.transaction_data())

    last_block_in_chain = blockchain.chain[-1]

    pubsub.broadcast_block(last_block_in_chain)

    return jsonify(last_block_in_chain.to_json())


@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    # {'recipient': 'foo', 'amount': 15}

    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(wallet, transaction_data['recipient'], transaction_data['amount'])
    else:
        transaction = Transaction(
        wallet, transaction_data['recipient'], transaction_data['amount'])

    print(f'transaction.to_json: {transaction.to_json()}')

    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())

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
