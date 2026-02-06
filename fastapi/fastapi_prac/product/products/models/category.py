from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

# Product를 직접 import 하지 않고, 문자열로 처리하기 위해 TYPE_CHECKING 사용 가능하지만,
# SQLModel에서는 간단히 문자열 "Product"로 타입을 지정하면 해결됩니다.


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False)

    # List["Product"] 처럼 따옴표를 씁니다. (지연 평가)
    products: List["Product"] = Relationship(back_populates="category")
