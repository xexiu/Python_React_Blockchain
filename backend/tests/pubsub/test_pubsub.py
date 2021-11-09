import pytest
from backend.blockchain.blockchain import Blockchain
from backend.wallet.transaction_pool import TransactionPool
from backend.pubsub.pubsub import PubSub

blockchain = Blockchain()
transaction_pool = TransactionPool()
dummy_pubKey = 'pub-1234'
dummy_subKey = 'sub-1234'


@pytest.fixture
def pubSubDummy():
    return PubSub(blockchain, transaction_pool, dummy_subKey, dummy_pubKey)


def test_pubsub_config(pubSubDummy):
    assert pubSubDummy.pubKey == dummy_pubKey
    assert pubSubDummy.subKey == dummy_subKey
