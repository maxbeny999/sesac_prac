from fastapi import APIRouter, Query, Path, status
from typing import Annotated
from products.schemas.product import (
    ProductCreate,
    ProductDetailResponse,
    ProductListResponse,
)
from products.service.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])
service = ProductService()


@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=ProductDetailResponse
)
def create_product(product_req: ProductCreate):
    return service.create_product(product_req)


@router.get("", response_model=list[ProductListResponse])
def get_products(
    keyword: Annotated[str | None, Query(min_length=2)] = None,
    category: Annotated[str | None, Query(alias="p-category")] = None,  # Alias 적용
    limit: int = 20,
):
    return service.get_products(keyword, category, limit)


@router.get("/{product_id}", response_model=ProductDetailResponse)
def get_product(product_id: int = Path(..., gt=0)):
    return service.get_product(product_id)
