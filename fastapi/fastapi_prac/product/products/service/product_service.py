from fastapi import HTTPException
from products.repository.product_repository import ProductRepository
from products.repository.category_repository import CategoryRepository
from products.models import Product
from products.schemas.product import (
    ProductCreate,
    ProductDetailResponse,
    ProductListResponse,
)
from products.schemas.category import CategoryRead


class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()
        self.category_repo = CategoryRepository()

    def create_product(self, product_req: ProductCreate):
        # 1. 카테고리 존재 확인
        category = self.category_repo.get_by_name(product_req.category_name)
        if not category:
            raise HTTPException(status_code=404, detail="존재하지 않는 카테고리입니다.")

        # 2. Product 모델 생성
        new_product = Product(
            name=product_req.name,
            price=product_req.price,
            discount_price=product_req.discount_price,
            stock=product_req.stock,
            category_id=category.id,
        )
        saved_product = self.product_repo.save(new_product)
        return self._to_detail_response(saved_product)

    def get_products(self, keyword, category_name, limit):
        products = self.product_repo.get_all(keyword, category_name, limit)
        return [self._to_list_response(p) for p in products]

    def get_product(self, product_id):
        product = self.product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
        return self._to_detail_response(product)

    # 응답 변환 로직 (계산된 필드 처리)
    def _to_detail_response(self, p: Product):
        return ProductDetailResponse(
            id=p.id,
            name=p.name,
            final_price=p.price - p.discount_price,
            stock=p.stock,
            is_sold_out=p.stock <= 0,
            category=CategoryRead.model_validate(p.category),
        )

    def _to_list_response(self, p: Product):
        return ProductListResponse(
            id=p.id,
            name=p.name,
            final_price=p.price - p.discount_price,
            category=CategoryRead.model_validate(p.category),
        )
