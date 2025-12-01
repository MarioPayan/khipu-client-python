import requests
from dataclasses import asdict
from .data_classes import (
    PaymentResponse,
    ReceiverRequest,
    PaymentRequest,
    ReceiverResponse,
)


def post(self, url: str, request) -> dict:
    try:
        url = f"{self.base_url}/{url}"
        params = {k: v for k, v in asdict(request).items() if v is not None}
        headers = self.auth.get_headers("POST", url, params)
        response = requests.post(url, data=params, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.HTTPError as e:
        print("Request failed: ", e)
        print("Status: ", response.status_code)
        print("Body: ", response.text)
    except Exception as e:
        print("An unexpected error occurred: ", e)
    return data


def create_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
    data = post(self, "payments", payment_request)
    return PaymentResponse(**data)


def create_receiver(self, receiver_request: ReceiverRequest) -> ReceiverResponse:
    data = post(self, "receivers", receiver_request)
    return ReceiverResponse(**data)
