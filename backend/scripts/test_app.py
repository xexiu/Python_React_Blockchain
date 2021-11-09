import time

import requests
from backend.blockchain.blockchain import Blockchain
from backend.util.global_variables import BASE_URL, ONE_SECOND
from backend.wallet.wallet import Wallet

#  YOU MUST START THE SERVER BEFORE TESTING APP

MAP_REQUESTS = {
    'blockchain': requests.get(f'{BASE_URL}/blockchain').json(),  #  get
    'mine': requests.get(f'{BASE_URL}/blockchain/mine').json(),  #  get
    'wallet_info': requests.get(f'{BASE_URL}/wallet/info').json(),  #  get
    #  post
    'wallet_transaction': lambda recipient, amount: requests.post(f'{BASE_URL}/wallet/transact', json={'recipient': recipient, 'amount': amount}).json()
}


def get_blockchain():
    return MAP_REQUESTS['blockchain']


def get_blockchain_mine():
    return MAP_REQUESTS['mine']


def post_wallet_transaction(recipient, amount):
    return MAP_REQUESTS['wallet_transaction'](recipient, amount)


def get_wallet_info():
    return MAP_REQUESTS['wallet_info']


start_blockchain = get_blockchain()

print(f'start_blockchain: {start_blockchain}')

recipient = Wallet(Blockchain()).address

post_wallet_transact_1 = post_wallet_transaction(recipient, 21)
print(f'\npost_wallet_transact_1: {post_wallet_transact_1}')

time.sleep(ONE_SECOND)

post_wallet_transact_2 = post_wallet_transaction(recipient, 31)
print(f'\npost_wallet_transact_2: {post_wallet_transact_2}')

time.sleep(ONE_SECOND)

mined_block = get_blockchain_mine()
print(f'\nmined_block: {mined_block}')

wallet_info = get_wallet_info()
print(f'\nwallet_info: {wallet_info}')
