from block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self) -> str:
        return f'Blockcain: {self.chain}' # Blockcain: [<__main__.Block object at 0x100727520>, <__main__.Block object at 0x1007274c0>]

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')
    # <__main__.Blockchain object at 0x10dcc7610>

if __name__ == '__main__':
    main()
