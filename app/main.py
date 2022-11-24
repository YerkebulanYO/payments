# Standard Library
import logging
from typing import List

from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session

# App Imports
from .schemas import OrderRequest, OrderResponse
from .db import Base, engine
from . import crud
from .models import Order

app = FastAPI(
    title="FastAPI Application"
)

Base.metadata.create_all(engine)
#
#
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@app.get('/')
def func():
    """ This function for testing"""
    return {'Test': 'successful'}

#
# @app.get(
#     '/posts',
#     status_code=status.HTTP_200_OK,
#     description='return all the exists posts',
#     summary='Get all posts',
#     response_model=List[PostDB]
# )
# async def read_all_posts():
#     return await crud.get_all()


@app.get(
    '/order/{id}',
    status_code=status.HTTP_200_OK,
    summary='Get Order By ID',
    description='Получение заказа по ID',
    response_description='Заказ по айди передан'
    # response_model=OrderResponse,
)
async def get_order(
        order_id: int,
        db: Session = Depends(crud.get_db)):
    response = await crud.get(order_id, db)
    print(response.currency)
    return response

    # data = db.query(Order).get(id)
    #
    # if not data:
    #     return 'Not found'
    #
    # return data

    # post = await crud.get(id)
    # if post is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    # return post


@app.post(
    '/create-order',
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    description="Create an order, take a OrderRequest from merchant and return OrderResponse",
    summary="CreateOrder",
    response_description='Заказ создан'
)
async def create_order(
        order: OrderRequest,
        db: Session = Depends(crud.get_db)):
    response = await crud.post(order, db)

    return response

    # new_post = Post(**payload.dict())
    # new_order = Order(title=order.)
    # db.add(new_order)
    # db.commit()
    # db.refresh(new_order)

    # post_id = await crud.post(payload)
    #
    # response = {
    #     "id": post_id,
    #     "title": payload.title
    # }
    #
    # return response
