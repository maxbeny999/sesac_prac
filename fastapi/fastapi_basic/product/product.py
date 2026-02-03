from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int

    product_name: str

    price: int


# 게시글 클래스
class Product:
    def __init__(self, id, product_name, price):
        self.id = id
        self.product_name = product_name
        self.price = price
