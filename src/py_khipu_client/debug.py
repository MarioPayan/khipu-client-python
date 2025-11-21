import os
import requests
from dotenv import load_dotenv
from .data_classes import PaymentRequest, ReceiverRequest
from .client import Client

if __name__ == "__main__":
    load_dotenv()
    receiver_id = int(os.getenv("KHIPU_RECEIVER_ID", "0"))
    secret = os.getenv("KHIPU_SECRET", "")
    client = Client(receiver_id=receiver_id, secret=secret)

    # Example 1: Create a payment
    print("=== Creating Payment ===")
    try:
        payment = client.create_payment(
            PaymentRequest(amount=1000, currency="CLP", subject="Cobro de prueba")
        )

        print(payment)

    except requests.exceptions.HTTPError as e:
        print(f"Error creating payment: {e}")
        print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Example 2: Create a receiver
    print("=== Creating Receiver ===")
    try:
        receiver = client.create_receiver(
            ReceiverRequest(
                admin_first_name="Nombre",
                admin_last_name="Apellido",
                admin_email="admin@email.com",
                country_code="CL",
                business_identifier="99.999.999-9",
                business_category="VENTA AL POR MAYOR DE FRUTAS Y VERDURAS",
                business_name="Nombre Tributario",
                business_phone="+56988887777",
                business_address_line_1="Calle principal 1111",
                business_address_line_2="Oficina 3-A",
                business_address_line_3="Santiago",
                contact_full_name="Nombre Contacto",
                contact_job_title="Tesorero",
                contact_email="contacto@email.com",
                contact_phone="+56955553333",
                notify_url="http://micomercio.com/account/notify_url",
                rendition_url="http://micomercio.com/account/rendition_url",
            )
        )

        print(receiver)

    except requests.exceptions.HTTPError as e:
        print(f"Error creating receiver: {e}")
        print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"Unexpected error: {e}")
