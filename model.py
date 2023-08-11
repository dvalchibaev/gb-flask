from datetime import datetime
from pydantic import BaseModel, Field


class ItemInput(BaseModel):
    name: str = Field(..., title="Item", min_length=1, max_length=100)
    description: str = Field(..., title="Description", min_length=1, max_length=500)
    price: float = Field(..., title="Price", ge=0)


class UserInput(BaseModel):
    name: str = Field(..., title="name", min_length=1, max_length=100)
    last_name: str = Field(..., title="last_name", min_length=1, max_length=100)
    email: str = Field(..., title="email", min_length=4, max_length=100)
    password: str = Field(..., title="password", min_length=4, max_length=100)


class OrderInput(BaseModel):
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    order_date: str = Field(..., min_length=19, max_length=19)
    status: str = Field(default="Not initiated", max_length=1000)


class Item(BaseModel):
    id: int = Field(..., ge=0)
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., max_length=500)
    price: float = Field(..., ge=0)


class User(BaseModel):
    id: int = Field(..., ge=0)
    name: str = Field(..., title="name", min_length=1, max_length=100)
    last_name: str = Field(..., title="last_name", min_length=1, max_length=100)
    email: str = Field(..., title="email", min_length=4, max_length=100)
    password: str = Field(..., title="password", min_length=4, max_length=100)


class Order(BaseModel):
    id: int = Field(..., ge=0)
    user_id: int = Field(..., ge=0)
    item_id: int = Field(..., ge=0)
    order_date: str = Field(..., min_length=19, max_length=19)
    status: str = Field(default="Not initiated", max_length=1000)
