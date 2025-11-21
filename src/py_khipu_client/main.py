"""
Khipu Client - Main entry point for CLI usage (optional)
"""

from .client import Client


def main(receiver_id: int, secret: str) -> Client:
    """
    Create and return a Khipu client instance.

    Args:
        receiver_id: Your Khipu receiver ID
        secret: Your Khipu secret key

    Returns:
        Client: Configured Khipu client instance
    """
    return Client(receiver_id=receiver_id, secret=secret)
