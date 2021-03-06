import time

from backend.util.config import MIN_RATE
from backend.util.crypto_hash import crypto_hash
from backend.util.global_variables import GENESIS_DATA
from backend.util.hex_to_binary import hex_to_binary


class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp: int, last_hash: str, hash: str, data: list, difficulty: int, nonce: str) -> None:
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self) -> str:
        return (
            'Block('
            f'timestamp: {self.timestamp} '
            f'last_hash: {self.last_hash} '
            f'hash: {self.hash} '
            f'data: {self.data}) ',
            f'difficulty: {self.difficulty}) ',
            f'nonce: {self.nonce})',
        )

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    @staticmethod
    def mine_block(last_block: classmethod, data: str) -> classmethod:
        """
        Mine a block based on the given last_block and data
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis() -> classmethod:
        """
        Generate the Genesis Block
        # return Block(GENESIS_DATA['timestamp'], GENESIS_DATA['last_hash'], GENESIS_DATA['hash'], GENESIS_DATA['data'])
        """

        return Block(**GENESIS_DATA)

    def adjust_difficulty(last_block: classmethod, new_timestamp: int) -> int:
        """
        Calculate the difficulty depending on the MINE_RATE
        Increase the difficulty for quickly mined blocks
        Decrese the difficulty for slowly mined blocks
        """

        if(new_timestamp < last_block.timestamp) < MIN_RATE:
            return last_block.difficulty + 1

        if(last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

    @staticmethod
    def is_valid_block(last_block: classmethod, block: classmethod) -> bool:
        if(block.last_hash != last_block.hash):
            raise Exception('The block last_hash must be correct!')
        if(hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty):
            raise Exception('The proof of work requirement was not met!')
        if(abs(last_block.difficulty - block.difficulty) > 1):
            raise Exception('The block difficulty must only adjust by 1!')

        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.difficulty,
            block.nonce
        )

        if(block.hash != reconstructed_hash):
            raise Exception('The block hash must be correct!')

    def to_json(self) -> object:
        return self.__dict__

    def from_json(block_json):
        return Block(**block_json)


def main():
    genesis_block = Block.genesis()
    bad_block = Block.mine_block(genesis_block, 'foo')
    bad_block.last_hash = 'evil_data'

    try:
        Block.is_valid_block(genesis_block, bad_block)
    except Exception as e:
        print(f'is_valid_block: {e}')

if __name__ == '__main__':
    main()
