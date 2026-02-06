from pydantic import BaseModel, Field, model_validator, ConfigDict
from .category import CategoryRead


class ProductCreate(BaseModel):
    # alias 적용: 클라이언트는 "product_name"으로 보냄 -> 코드는 name으로 받음
    name: str = Field(..., alias="product_name", min_length=2, max_length=50)
    price: int = Field(..., ge=100)
    discount_price: int = Field(0, ge=0)
    stock: int = Field(10, ge=0)
    category_name: str  # 등록할 땐 이름으로 받음

    model_config = ConfigDict(populate_by_name=True)

    @model_validator(mode="after")
    def check_discount_price(self):
        if self.discount_price >= self.price:
            raise ValueError("할인 금액은 상품 원가보다 작아야 합니다.")
        return self


class ProductUpdate(ProductCreate):
    pass


class ProductListResponse(BaseModel):
    id: int
    name: str
    final_price: int
    category: CategoryRead  # Nested Schema

    model_config = ConfigDict(from_attributes=True)


class ProductDetailResponse(ProductListResponse):
    stock: int
    is_sold_out: bool
