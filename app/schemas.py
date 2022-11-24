from pydantic import BaseModel, validator, ValidationError
from pydantic.typing import Optional
from enum import Enum

from .models import CurrencyEnum


class OrderDB(BaseModel):
    """
    Model to save in db.
    """
    amount: int
    currency: str
    market_ord_id: str
    description: Optional[str]
    merch_name: str
    merchant_id: str
    mac: str
    trtype: int  # Тоже enum


class OrderRequest(BaseModel):
    """
    Request to create an order from merchant.
    """
    '''
    Todo: надо композировать
    '''
    amount: int
    currency: str
    market_order_id: int  # ORDER
    description: Optional[str] = None
    merch_name: str
    merch_url: str
    merchant: str
    terminal: str
    email: str
    notify_url: str
    country: str
    merch_gmt: str
    timestamp: str
    nonce: str
    backref: str
    p_sign: str
    trtype: int  # Тоже enum

    @validator('amount')
    def amount_higher_than_100(cls, amount):
        if amount < 100:
            raise ValueError('amount must be higher than 100')
        return amount

    @validator('currency')
    def exists_currency(cls, currency):
        if currency not in ('RUB', 'KZT', 'USD'):
            raise ValueError('not exist currency')
        return currency


class OrderResponse(BaseModel):
    """
    Response to merchant after creating an order.
    """
    id: int
    amount: int
    description: str


# class OrderResponse(BaseModel):
#     """
#     Response to merchant after creating an order.
#     """
#     '''
#     Todo: надо композировать
#     '''
#     terminal: str
#     trtype: int  # Тоже enum
#     market_order_id: str  # ORDER
#     amount: int
#     currency: str
#     action: int
#     rc: int
#     approval: int
#     rrn: str
#     int_ref: str
#     timestamp: str
#     nonce: str
#     p_sign: str
