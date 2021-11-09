from backend.blockchain.block import Block
from backend.util.global_variables import CHANNELS
from pubnub.callbacks import SubscribeCallback


class Listener(SubscribeCallback):
    def __init__(self, blockchain: list, transaction_pool) -> None:
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool

    def message(self, pubnub, message: str):
        print(f'-- Channel: {message.channel} | Message: {message.message}')

        if(message.channel == CHANNELS['BLOCK']):
            block = Block.from_json(message.message)
            #  Attr [:] doest an exact copy of the list
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                raise Exception(f'Could not replace chain: {e}')
        elif message.channel == CHANNELS['TRANSACTION']:


        return super().message(pubnub, message)
