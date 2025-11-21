import requests
from dataclasses import asdict
from .data_classes import (
    PaymentResponse,
    ReceiverRequest,
    PaymentRequest,
    ReceiverResponse,
)


def create_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
    url = f"{self.base_url}/payments"
    params = {k: v for k, v in asdict(payment_request).items() if v is not None}
    headers = self.auth.get_headers("POST", url, params)
    response = requests.post(url, data=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return PaymentResponse(**data)


def create_receiver(self, receiver_request: ReceiverRequest) -> ReceiverResponse:
    url = f"{self.base_url}/receivers"
    params = {k: v for k, v in asdict(receiver_request).items() if v is not None}
    headers = self.auth.get_headers("POST", url, params)
    response = requests.post(url, data=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return ReceiverResponse(**data)
