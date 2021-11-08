import time

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

from backend.blockchain.block import Block
from backend.util.global_variables import CHANNELS, CONFIG_PN


class Listener(SubscribeCallback):
    def __init__(self, blockchain: list):
        self.blockchain = blockchain

    def message(self, pubnub, message: str):
        print(f'-- Channel: {message.channel} | Message: {message.message}')

        if(message.channel == CHANNELS['BLOCK']):
            block = Block.from_json(message.message)
            potential_chain = self.blockchain.chain[:] # Attr [:] doest an exact copy of the list
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                raise Exception(f'Could not replace chain: {e}')

        return super().message(pubnub, message)

class PubSub():
    def __init__(self, blockchain, subKey: str, pubKey: str):
        self.subKey = subKey
        self.pubKey = pubKey
        self.pnconfig = self.config()
        self.pubnub = PubNub(self.pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def config(self):
        self.pnconfig = PNConfiguration()
        self.pnconfig.subscribe_key = self.subKey
        self.pnconfig.publish_key = self.pubKey

        return self.pnconfig

    def publish(self, channel: str, message: object):
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Broadcast a block to all nodes.
        """

        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    pubsub = PubSub([Block.genesis()], **CONFIG_PN)
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})

if __name__ == '__main__':
    main()
