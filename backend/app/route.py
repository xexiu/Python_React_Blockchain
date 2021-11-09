import requests
from backend.blockchain.blockchain import Blockchain
from backend.pubsub.pubsub import PubSub
from backend.util.global_variables import CONFIG_PN, ROOT_PORT
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.wallet import Wallet
from flask import Flask, jsonify, request


class Route:
    def __init__(self, name) -> None:
        self.app = Flask(name)
        self.blockchain = Blockchain()
        self.transaction_pool = TransactionPool()
        self.pubsub = PubSub(
            self.blockchain, self.transaction_pool, **CONFIG_PN)
        self.wallet = Wallet(self.blockchain)

    def default():
        return 'Welcome to Homepage'

    def route_blockchain(self):
        return jsonify(self.blockchain.to_json())

    def route_blockchain_mine(self):
        transaction_data = self.transaction_pool.transaction_data()
        transaction_data.append(Transaction.reward_transaction(self.wallet).to_json())
        
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

    def get_new_chain(self):
        result = requests.get(f'http://127.0.0.1:{ROOT_PORT}/blockchain')
        result_blockchain = Blockchain.from_json(result.json())

        try:
            self.blockchain.replace_chain(result_blockchain.chain)
            print('\n -- Successfully synchronized the local chain')
        except Exception as e:
            print(f'\n -- Error synchronizing: {e}')
