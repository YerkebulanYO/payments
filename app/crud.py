from sqlalchemy.orm import Session
# from db import database, Session

from .models import Order
from .schemas import OrderDB, OrderRequest
from .db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def post(
        order: OrderRequest,
        db: Session) -> dict:
    # query = posts.insert().values(data.json())
    # return await database.execute(query=query)
    data = Order(
        amount=order.amount,
        currency=order.currency,
        market_ord_id=order.market_order_id,
        description=order.description,
        merch_name=order.merch_name,
        merchant_id=order.merchant,
        mac=order.p_sign,
        trtype=order.trtype
    )

    db.add(data)
    db.commit()
    db.refresh(data)

    #  пока не знаю что можно возвращать
    print(data.id)
    return {'id': data.id, 'amount': data.amount, 'description': data.description}


async def get(id: int,
              db: Session):
    response = db.query(Order).get(id)

    if not response:
        return "Not found"

    return response

    # data = orders.select().where(
    #     posts.id == id
    # ).first()
    #
    # return data


    # query = Post.select().where(id == Post.c.id)
    # return await database.fetch_one(query=query)


# async def get_all():
#     query = Post.select()
#     return await database.fetch_all(query=query)

# put and delete
