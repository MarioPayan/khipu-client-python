from .auth import Auth
from .endpoints import create_payment, create_receiver


class Client:
    def __init__(
        self,
        receiver_id: int,
        secret: str,
        base_url: str = "https://khipu.com/api",
        api_version: str = "2.0",
    ):
        self.base_url = f"{base_url}/{api_version}"
        self.auth = Auth(receiver_id, secret)

    create_payment = create_payment
    create_receiver = create_receiver
