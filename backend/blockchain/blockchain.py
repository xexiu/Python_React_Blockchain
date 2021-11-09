from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self) -> None:
        self.chain = [Block.genesis()]

    def add_block(self, data: str):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self) -> str:
        return f'Blockcain: {self.chain}'

    def replace_chain(self, chain: list):
        if(len(chain) <= len(self.chain)):
            raise Exception('Cannot replace. The incoming chain must be longer')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming chain is invalid: {e}')

        self.chain = chain

    @staticmethod
    def is_valid_chain(chain: list) -> bool:
        if(chain[0] != Block.genesis()):
            raise Exception('The genesis block must be valid!')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            Block.is_valid_block(last_block, block)

    def to_json(self):
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        blockchain = Blockchain()
        blockchain.chain = list(map(lambda block_json: Block.from_json(block_json), chain_json))

        return blockchain



def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')
    # <__main__.Blockchain object at 0x10dcc7610>

if __name__ == '__main__':
    main()
