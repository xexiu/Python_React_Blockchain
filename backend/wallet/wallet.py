import json
import uuid

from backend.util.config import STARTING_BALANCE
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    decode_dss_signature, encode_dss_signature)


class Wallet:
    def __init__(self, blockchain=None) -> None:
        self.blockchain = blockchain
        self.address: str = str(uuid.uuid4())[0:8]
        self.private_key: str = ec.generate_private_key(
            ec.SECP256R1(), default_backend())
        self.public_key: str = self.private_key.public_key()
        self.public_key = self.serialize_public_key()

    @property
    def balance(self):
        return Wallet.calculate_balance(self.blockchain, self.address)

    def sign(self, data: any):
        return decode_dss_signature(self.private_key.sign(json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256())))

    def serialize_public_key(self):
        return self.public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('utf-8')

    def deserialized_public_key(public_key):
        return serialization.load_pem_public_key(public_key.encode('utf-8'), default_backend())

    @staticmethod
    def verify(public_key: str, data: any, signature: str):

        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'), default_backend())
        (r, s) = signature

        try:
            deserialized_public_key.verify(encode_dss_signature(r, s), json.dumps(
                data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False

    @staticmethod
    def calculate_balance(blockchain, address):
        balance = STARTING_BALANCE

        if not blockchain:
            return balance

        for block in blockchain.chain:
            for transaction in block.data:
                if transaction['input']['address'] == address:
                    balance = transaction['output'][address]
                elif address in transaction['output']:
                    balance += transaction['output'][address]
        return balance


def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}')
    data = {
        'foo': 'bar'
    }

    signature = wallet.sign(data)
    print(f'signature: {signature} {type(signature)}')

    should_be_valid = wallet.verify(wallet.public_key, data, signature)
    print(f'should_be_valid: {should_be_valid}')

    should_be_invalid = wallet.verify(Wallet().public_key, data, signature)
    print(f'should_be_invalid: {should_be_invalid}')


if __name__ == '__main__':
    main()
