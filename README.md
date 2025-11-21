# Khipu Python Client

A Python client library for the [Khipu](https://khipu.com) payment API. Khipu is a popular payment platform in Latin America that enables businesses to accept payments easily.

## Features

- 🔐 Secure authentication using HMAC-SHA256
- 💳 Create payment requests
- 🏢 Create receiver accounts
- 📦 Simple, intuitive API
- 🐍 Type hints for better IDE support
- ✅ Dataclass-based request/response models

## Installation

```bash
pip install khipu
```

## Quick Start

```python
from khipu import Client
from khipu.data_classes import PaymentRequest

# Initialize the client
client = Client(
    receiver_id=12345,
    secret="your-secret-key"
)

# Create a payment
payment_request = PaymentRequest(
    amount=1000,
    currency="CLP",
    subject="Test Payment",
    transaction_id="ORDER-123",
    return_url="https://yoursite.com/success",
    cancel_url="https://yoursite.com/cancel",
    notify_url="https://yoursite.com/webhook"
)

payment_response = client.create_payment(payment_request)
print(f"Payment URL: {payment_response.payment_url}")
```

## Usage

### Creating a Client

```python
from khipu import Client

client = Client(
    receiver_id=12345,
    secret="your-secret-key",
    base_url="https://khipu.com/api",  # Optional, default value
    api_version="2.0"  # Optional, default value
)
```

### Creating a Payment

```python
from khipu.data_classes import PaymentRequest

payment_request = PaymentRequest(
    amount=5000,
    currency="CLP",
    subject="Product Purchase",
    body="Detailed description of the purchase",
    transaction_id="UNIQUE-ORDER-ID",
    payer_email="customer@example.com",
    return_url="https://yoursite.com/success",
    cancel_url="https://yoursite.com/cancel",
    notify_url="https://yoursite.com/webhook",
    expires_date="2024-12-31T23:59:59"
)

response = client.create_payment(payment_request)

# Redirect user to payment_url
print(response.payment_url)
```

### Creating a Receiver

```python
from khipu.data_classes import ReceiverRequest

receiver_request = ReceiverRequest(
    admin_first_name="John",
    admin_last_name="Doe",
    admin_email="admin@example.com",
    country_code="CL",
    business_identifier="12345678-9",
    business_category="services",
    business_name="My Business",
    business_phone="+56912345678",
    business_address_line_1="Address Line 1",
    business_address_line_2="Address Line 2",
    business_address_line_3="City, Region",
    contact_full_name="Jane Doe",
    contact_job_title="Manager",
    contact_email="contact@example.com",
    contact_phone="+56987654321"
)

receiver_response = client.create_receiver(receiver_request)
print(f"Receiver ID: {receiver_response.receiver_id}")
```

## API Reference

### PaymentRequest

Required fields:
- `amount` (int): Amount in the smallest currency unit (e.g., cents)
- `currency` (str): Currency code (e.g., "CLP", "USD")
- `subject` (str): Payment subject/title

Optional fields:
- `transaction_id` (str): Unique transaction identifier
- `custom` (str): Custom data
- `body` (str): Payment description
- `bank_id` (str): Specific bank ID
- `return_url` (str): URL to redirect after successful payment
- `cancel_url` (str): URL to redirect after cancelled payment
- `picture_url` (str): URL of product/service image
- `notify_url` (str): Webhook URL for payment notifications
- `payer_email` (str): Payer's email address
- And more...

### PaymentResponse

- `payment_id` (str): Unique payment identifier
- `payment_url` (str): URL to redirect user for payment
- `simplified_transfer_url` (str): Simplified transfer URL
- `transfer_url` (str): Transfer URL
- `app_url` (str): Mobile app URL
- `ready_for_terminal` (bool): Whether payment is ready for terminal

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/MarioPayan/Zaku.git
cd Zaku/khipu

# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Format code
black .

# Lint code
flake8 .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Links

- [Khipu Official Website](https://khipu.com)
- [Khipu API Documentation](https://khipu.com/page/api)
- [GitHub Repository](https://github.com/MarioPayan/Zaku)

## Support

For issues and questions:
- Open an issue on [GitHub](https://github.com/MarioPayan/Zaku/issues)
- Contact Khipu support for API-related questions

## Disclaimer

This is an unofficial client library. For official support and documentation, please refer to [Khipu's official documentation](https://khipu.com/page/api).
