import json
import random

import requests
from backend.blockchain.blockchain import Blockchain
from backend.pubsub.pubsub import PubSub
from backend.util.global_variables import CONFIG_PN, ROOT_PORT
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.wallet import Wallet
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

with open('jokes/index.json', 'r') as myfile:
    data = myfile.read()

# parse file
jokes = json.loads(data)


class Route:
    def __init__(self, name) -> None:
        self.app = Flask(name)
        CORS(self.app, resources={
             r"/*": {"origins": "http://localhost:3000"}}, support_credentials=True)
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.blockchain = Blockchain()
        self.transaction_pool = TransactionPool()
        self.pubsub = PubSub(
            self.blockchain, self.transaction_pool, **CONFIG_PN)
        self.wallet = Wallet(self.blockchain)

    def default(_Self):
        return 'Welcome to Homepage'

    def route_blockchain(self):
        return jsonify(self.blockchain.to_json())

    def route_blockchain_mine(self):
        transaction_data = self.transaction_pool.transaction_data()
        transaction_data.append(
            Transaction.reward_transaction(self.wallet).to_json())

        self.blockchain.add_block(transaction_data)

        last_block_in_chain = self.blockchain.chain[-1]

        self.pubsub.broadcast_block(last_block_in_chain)
        self.transaction_pool.clear_blockchain_transaction(self.blockchain)

        return jsonify(last_block_in_chain.to_json())

    def route_wallet_transact(self):
        # {'recipient': 'foo', 'amount': 15}

        transaction_data = request.get_json()
        transaction = self.transaction_pool.existing_transaction(
            self.wallet.address)

        if transaction:
            transaction.update(
                self.wallet, transaction_data['recipient'], transaction_data['amount'])
        else:
            transaction = Transaction(
                self.wallet, transaction_data['recipient'], transaction_data['amount'])

        print(f'transaction.to_json: {transaction.to_json()}')

        self.pubsub.broadcast_transaction(transaction)

        return jsonify(transaction.to_json())

    def route_wallet_info(self):
        return jsonify({'address': self.wallet.address, 'balance': self.wallet.balance})

    def route_random_jokes(self):
        random_array_item = random.choice(jokes)
        response = jsonify(random_array_item)
        return response

    def route_blockchain_page(self):
        # http://127.0.0.1:5000/blockchain/page?start=2&end=5
        start = int(request.args.get('start'))
        end = int(request.args.get('end'))

        # To reverse a list:
        # foo = [1, 2, 3, 4]
        # foo[::-1] --> [4, 3, 2, 1]

        return jsonify(self.blockchain.to_json()[::-1][start:end])

    def route_blockchain_length(self):
        return jsonify(len(self.blockchain.chain))

    def route_known_addresses(self):
        known_addresses = set()

        for block in self.blockchain.chain:
            for transaction in block.data:
                known_addresses.update(transaction['output'].keys())

        return jsonify(list(known_addresses))

    def route_transactions(self):
        return jsonify(self.transaction_pool.transaction_data())

    def seed_data(self):
        for i in range(10):
            self.blockchain.add_block([
                Transaction(Wallet(), Wallet().address,
                            random.randint(2, 50)).to_json(),
                Transaction(Wallet(), Wallet().address,
                            random.randint(2, 50)).to_json()
            ])

        for i in range(3):
            self.transaction_pool.set_transaction(
                Transaction(Wallet(), Wallet().address, random.randint(2, 50))
            )

    def get_new_chain(self):
        result = requests.get(f'http://127.0.0.1:{ROOT_PORT}/blockchain')
        result_blockchain = Blockchain.from_json(result.json())

        try:
            self.blockchain.replace_chain(result_blockchain.chain)
            print('\n -- Successfully synchronized the local chain')
        except Exception as e:
            print(f'\n -- Error synchronizing: {e}')
