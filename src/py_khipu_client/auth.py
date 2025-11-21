from urllib.parse import quote
from typing import Dict, Any


class Auth:
    def __init__(self, receiver_id: int, secret: str):
        self.receiver_id = receiver_id
        self.secret = secret

    def _percent_encode(self, value: str) -> str:
        if value is None:
            return ""
        return quote(str(value), safe="")

    def _calculate_signature(
        self, method: str, url: str, params: Dict[str, Any]
    ) -> str:
        import hmac
        import hashlib

        to_sign = f"{method.upper()}&{self._percent_encode(url)}"
        sorted_keys = sorted(params.keys())

        for key in sorted_keys:
            to_sign += (
                f"&{self._percent_encode(key)}={self._percent_encode(params[key])}"
            )

        signature = hmac.new(
            self.secret.encode("utf-8"), to_sign.encode("utf-8"), hashlib.sha256
        ).hexdigest()

        return signature

    def _get_auth_header(self, method: str, url: str, params: Dict[str, Any]) -> str:
        signature = self._calculate_signature(method, url, params)
        return f"{self.receiver_id}:{signature}"

    def get_headers(
        self, method: str, url: str, params: Dict[str, Any]
    ) -> Dict[str, str]:
        auth_header = self._get_auth_header(method, url, params)
        return {
            "Authorization": auth_header,
            "Content-Type": "application/x-www-form-urlencoded",
        }
