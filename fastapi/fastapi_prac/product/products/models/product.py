from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    discount_price: int = Field(default=0)
    stock: int = Field(default=10)
    category_id: int = Field(foreign_key="categories.id")

    # 여기서도 "Category" 처럼 따옴표를 씁니다.
    category: Optional["Category"] = Relationship(back_populates="products")
