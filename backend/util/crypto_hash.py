import hashlib
import json


def crypto_hash(*args: any) -> str:
    """
    Return a sha-256 of the given arguments *args
    """

    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('foo'): {crypto_hash('foo')}")

if __name__ == '__main__':
    main()
