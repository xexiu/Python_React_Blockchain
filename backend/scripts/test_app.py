import time

import requests
from backend.util.global_variables import BASE_URL, ONE_SECOND
from backend.wallet.wallet import Wallet


def get_blockchain():
    return requests.get(f'{BASE_URL}/blockchain').json()


def get_blockchain_mine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()


def post_wallet_transaction(recipient, amount):
    return requests.post(f'{BASE_URL}/wallet/transact', json={'recipient': recipient, 'amount': amount}).json()


start_blockchain = get_blockchain()

print(f'start_blockchain: {start_blockchain}')

recipient = Wallet().address

post_wallet_transact_1 = post_wallet_transaction(recipient, 21)
print(f'\npost_wallet_transact_1: {post_wallet_transact_1}')

post_wallet_transact_2 = post_wallet_transaction(recipient, 31)
print(f'\npost_wallet_transact_2: {post_wallet_transact_2}')

time.sleep(ONE_SECOND)

mined_block = get_blockchain_mine()
print(f'\nmined_block: {mined_block}')
