"""
Example usage of the Khipu Python client
"""

from . import Client, PaymentRequest, ReceiverRequest


def create_simple_payment():
    """Example: Create a simple payment"""

    # Initialize client with your credentials
    client = Client(
        receiver_id=12345,  # Replace with your receiver ID
        secret="your-secret-key",  # Replace with your secret
    )

    # Create a payment request
    payment_request = PaymentRequest(
        amount=1000,  # Amount in smallest currency unit (e.g., cents)
        currency="CLP",
        subject="Test Payment",
    )

    # Create the payment
    response = client.create_payment(payment_request)

    print("Payment created successfully!")
    print(f"Payment ID: {response.payment_id}")
    print(f"Payment URL: {response.payment_url}")
    print(f"\nRedirect your user to: {response.payment_url}")

    return response


def create_detailed_payment():
    """Example: Create a payment with all optional parameters"""

    client = Client(receiver_id=12345, secret="your-secret-key")

    payment_request = PaymentRequest(
        # Required fields
        amount=5000,
        currency="CLP",
        subject="Premium Subscription",
        # Optional fields
        body="Monthly premium subscription for John Doe",
        transaction_id="ORDER-2024-001",
        payer_email="customer@example.com",
        payer_name="John Doe",
        return_url="https://yoursite.com/payment/success",
        cancel_url="https://yoursite.com/payment/cancel",
        notify_url="https://yoursite.com/webhooks/khipu",
        picture_url="https://yoursite.com/images/product.jpg",
        expires_date="2024-12-31T23:59:59",
    )

    response = client.create_payment(payment_request)

    print("Detailed payment created!")
    print(f"Payment URL: {response.payment_url}")

    return response


def create_receiver_account():
    """Example: Create a new receiver account"""

    # Note: Usually you don't need this unless you're creating sub-accounts
    client = Client(receiver_id=12345, secret="your-secret-key")

    receiver_request = ReceiverRequest(
        # Admin information
        admin_first_name="John",
        admin_last_name="Doe",
        admin_email="admin@example.com",
        # Business information
        country_code="CL",
        business_identifier="12345678-9",
        business_category="services",
        business_name="My Business SPA",
        business_phone="+56912345678",
        business_address_line_1="Av. Principal 123",
        business_address_line_2="Oficina 456",
        business_address_line_3="Santiago, Región Metropolitana",
        # Contact information
        contact_full_name="Jane Doe",
        contact_job_title="Finance Manager",
        contact_email="contact@example.com",
        contact_phone="+56987654321",
    )

    response = client.create_receiver(receiver_request)

    print("Receiver created successfully!")
    print(f"Receiver ID: {response.receiver_id}")
    print(f"Secret: {response.secret}")
    print("\nStore these credentials securely!")

    return response


def main():
    """Run examples"""

    print("=" * 60)
    print("Khipu Python Client - Examples")
    print("=" * 60)
    print()

    print("Example 1: Simple Payment")
    print("-" * 60)
    try:
        # Uncomment to run:
        # create_simple_payment()
        print("(Uncomment the function call to run)")
    except Exception as e:
        print(f"Error: {e}")

    print()
    print("Example 2: Detailed Payment")
    print("-" * 60)
    try:
        # Uncomment to run:
        # create_detailed_payment()
        print("(Uncomment the function call to run)")
    except Exception as e:
        print(f"Error: {e}")

    print()
    print("=" * 60)
    print("Remember to replace the credentials with your actual Khipu API keys!")
    print("=" * 60)


if __name__ == "__main__":
    main()
