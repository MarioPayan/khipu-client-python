from .client import Client


def main(receiver_id: int, secret: str) -> Client:
    return Client(receiver_id=receiver_id, secret=secret)
