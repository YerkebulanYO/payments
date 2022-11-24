import enum
from sqlalchemy import String, Integer, Column, Enum

from .db import Base


class CurrencyEnum(str, enum.Enum):
    KZT = "KZT"
    RUB = "RUB"
    USD = "USD"


class Order(Base):
    """
    This table is used for useful data for db.
    """
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    amount = Column(Integer)  # AMOUNT Цифра будет в тиын (500тг = 50000 тиын)
    currency = Column(Enum(CurrencyEnum), nullable=False)  # CURRENCY
    market_ord_id = Column(Integer())  # ORDER
    description = Column(String(50))  # DESCRIPTION
    merch_name = Column(String(50))  # MERCH_NAME
    merchant_id = Column(String(8))  # MERCHANT
    mac = Column(String(256))  # P_SIGN
    trtype = Column(Integer)  # TR_TYPE Тоже надо делать enum


orders = Order.__table__
