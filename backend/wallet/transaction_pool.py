class TransactionPool:
    def __init__(self) -> None:
        self.transaction_map = {}

    def set_transaction(self, transaction):
        self.transaction_map[transaction.id] = transaction
