import pytest
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

blockchain = Blockchain()
dummy_pubKey = 'pub-1234'
dummy_subKey = 'sub-1234'


@pytest.fixture
def pubSubDummy():
    return PubSub(blockchain, dummy_subKey, dummy_pubKey)


def test_pubsub_config(pubSubDummy):
    assert pubSubDummy.pubKey == dummy_pubKey
    assert pubSubDummy.subKey == dummy_subKey
