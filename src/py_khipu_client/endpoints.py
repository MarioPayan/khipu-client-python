import requests
from dataclasses import asdict
from typing import Type, TypeVar
from .data_classes import (
    PaymentResponse,
    ReceiverRequest,
    PaymentRequest,
    ReceiverResponse,
    ErrorResponse,
    ValidationError,
)

T = TypeVar("T")


def _post(
    self, endpoint: str, request_data, response_class: Type[T]
) -> T | ErrorResponse:
    url = f"{self.base_url}{endpoint}"
    params = {k: v for k, v in asdict(request_data).items() if v is not None}
    headers = self.auth.get_headers("POST", url, params)
    response = requests.post(url, data=params, headers=headers)
    data = response.json()

    if response.status_code in (200, 201):
        return response_class(**data)

    if response.status_code in range(400, 600):
        errors = [ValidationError(**error) for error in data.get("errors", [])]
        return ErrorResponse(
            status=data["status"], message=data["message"], errors=errors
        )
    return ErrorResponse(
        status=response.status_code,
        message="Unexpected error",
        errors=[],
    )


def create_payment(
    self, payment_request: PaymentRequest
) -> PaymentResponse | ErrorResponse:
    return _post(self, "/payments", payment_request, PaymentResponse)


def create_receiver(
    self, receiver_request: ReceiverRequest
) -> ReceiverResponse | ErrorResponse:
    return _post(self, "/receivers", receiver_request, ReceiverResponse)
