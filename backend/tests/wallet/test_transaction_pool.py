from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.wallet import Wallet


def test_set_transaction():
    transaction_pool = TransactionPool()
    sender_wallet = Wallet()
    transaction = Transaction(sender_wallet, 'recipient', 10)

    transaction_pool.set_transaction(transaction)

    assert transaction_pool.transaction_map[transaction.id] == transaction
