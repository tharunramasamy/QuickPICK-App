from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_id: int
    payment_method: str
    items: List[OrderItem]

class LoginRequest(BaseModel):
    username: str
    password: str