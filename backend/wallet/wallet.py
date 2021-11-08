import uuid
import json

from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


class Wallet:
    def __init__(self):
        self.address: str = str(uuid.uuid4())[0:8]
        self.balance: int = STARTING_BALANCE
        self.private_key: str = ec.generate_private_key(ec.SECP256R1(), default_backend())
        self.public_key: str = self.private_key.public_key()

    def sign(self, data: any):
        return self.private_key.sign(json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))

    @staticmethod
    def verify(public_key: str, data: any, signature: str):

        try:
            public_key.verify(signature, json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False



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
