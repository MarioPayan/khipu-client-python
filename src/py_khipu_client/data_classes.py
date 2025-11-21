from typing import Optional
from dataclasses import dataclass


@dataclass
class BaseDataClass:
    pass


@dataclass
class PaymentResponse(BaseDataClass):
    payment_id: str
    payment_url: str
    simplified_transfer_url: str
    transfer_url: str
    app_url: str
    ready_for_terminal: bool


@dataclass
class PaymentRequest(BaseDataClass):
    amount: int
    currency: str
    subject: str
    transaction_id: Optional[str] = None
    custom: Optional[str] = None
    body: Optional[str] = None
    bank_id: Optional[str] = None
    return_url: Optional[str] = None
    cancel_url: Optional[str] = None
    picture_url: Optional[str] = None
    notify_url: Optional[str] = None
    contract_url: Optional[str] = None
    notify_api_version: Optional[str] = None
    expires_date: Optional[str] = None
    send_email: Optional[bool] = None
    payer_name: Optional[str] = None
    payer_email: Optional[str] = None
    send_reminders: Optional[bool] = None
    responsible_user_email: Optional[str] = None
    fixed_payer_personal_identifier: Optional[str] = None
    integrator_fee: Optional[int] = None
    collect_account_uuid: Optional[str] = None
    confirm_timeout_date: Optional[str] = None
    mandatory_payment_method: Optional[str] = None


@dataclass
class ReceiverRequest(BaseDataClass):
    admin_first_name: str
    admin_last_name: str
    admin_email: str
    country_code: str
    business_identifier: str
    business_category: str
    business_name: str
    business_phone: str
    business_address_line_1: str
    business_address_line_2: str
    business_address_line_3: str
    contact_full_name: str
    contact_job_title: str
    contact_email: str
    contact_phone: str
    bank_account_bank_id: Optional[str] = None
    bank_account_type: Optional[str] = None
    bank_account_identifier: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_number: Optional[str] = None
    notify_url: Optional[str] = None
    rendition_url: Optional[str] = None


@dataclass
class ReceiverResponse(BaseDataClass):
    receiver_id: str
    secret: str
    contract_url: Optional[str] = None
