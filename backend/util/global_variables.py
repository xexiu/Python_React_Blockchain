ROOT_PORT: int = 5000
PORT: int = ROOT_PORT
PEER: str = 'PEER'
CHANNELS: dict[str, str] = {
    'TEST': 'TEST_CHANNEL',
    'BLOCK': 'BLOCK_CHANNEL'
}
CONFIG_PN: dict[str, str] = {
    'subKey': 'sub-c-0f0e7a52-2ffd-11ec-9682-f27e7ede0273',
    'pubKey': 'pub-c-701e95f0-5009-4b64-9b76-f20f7fe0727a'
}
GENESIS_DATA: dict[str, any] = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}
