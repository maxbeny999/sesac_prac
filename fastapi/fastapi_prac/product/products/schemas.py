from sqlmodel import SQLModel, Field
from pydantic import model_validator, ConfigDict
from typing import Optional


# 1. DB 엔티티 (저장용)
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    discount_price: int
    stock: int
    category: str


# 2. 요청 (Request) - 등록/수정 공용
class ProductCreate(SQLModel):
    # alias="product_name": 클라이언트는 "product_name"으로 보내지만, 파이썬에선 name으로 씀
    name: str = Field(min_length=2, max_length=50, alias="product_name")
    price: int = Field(ge=100)  # 100원 이상
    discount_price: int = Field(ge=0)  # 0원 이상
    stock: int = Field(default=10, ge=0)
    category: str = Field(min_length=2)

    # Pydantic 설정: alias를 써도 되고 원래 이름을 써도 되게 유연하게 설정
    model_config = ConfigDict(populate_by_name=True)

    # [검증 로직] 할인 금액이 원가보다 큰지 체크
    @model_validator(mode="after")
    def check_discount_price(self):
        if self.discount_price >= self.price:
            raise ValueError("할인 금액은 상품 원가보다 작아야 합니다.")
        return self


# 업데이트용 (Create와 같지만 일부만 받을 수도 있음 - 여기선 편의상 상속)
class ProductUpdate(ProductCreate):
    pass


# 3. 응답 (Response)
# 공통적으로 계산된 final_price가 필요하므로 부모 클래스 생성
class ProductResponseBase(SQLModel):
    id: int
    name: str
    category: str
    final_price: int  # 계산된 필드


# 목록 조회용 (심플)
class ProductListResponse(ProductResponseBase):
    pass


# 상세 조회용 (재고, 품절여부 포함)
class ProductDetailResponse(ProductResponseBase):
    stock: int
    is_sold_out: bool  # 계산된 필드
