import time

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

from backend.blockchain.block import Block
from backend.util.global_variables import CHANNELS, CONFIG_PN
from backend.pubsub.pubsub_listener import Listener

class PubSub():
    def __init__(self, blockchain, subKey: str, pubKey: str) -> None:
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
