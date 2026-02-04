# products/router.py
from fastapi import APIRouter, Query, Path, status
from typing import Annotated
from products.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductDetailResponse,
    ProductListResponse,
)
from products.service import product_service

router = APIRouter(prefix="/products")


# 1. 상품 등록
@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=ProductDetailResponse
)
def create_product(product_req: ProductCreate):
    return product_service.create_product(product_req)


# 2. 상품 상세 조회 (Path 검증: 1 이상)
@router.get("/{product_id}", response_model=ProductDetailResponse)
def get_product(product_id: Annotated[int, Path(gt=0, description="상품 ID (1 이상)")]):
    return product_service.get_product(product_id)


# 3. 상품 목록 조회 (Query 검증 및 Alias)
@router.get("", response_model=list[ProductListResponse])
def get_products(
    keyword: Annotated[str | None, Query(min_length=2)] = None,
    category: Annotated[
        str | None, Query(alias="p-category")
    ] = None,  # p-category -> category 매핑
    limit: Annotated[int, Query(le=100)] = 20,  # 최대 100개, 기본 20
):
    return product_service.get_products(keyword, category, limit)


# 4. 상품 수정
@router.put("/{product_id}", response_model=ProductDetailResponse)
def update_product(product_id: Annotated[int, Path(gt=0)], product_req: ProductUpdate):
    return product_service.update_product(product_id, product_req)
