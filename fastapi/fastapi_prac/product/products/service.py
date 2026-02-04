# products/service.py
from fastapi import HTTPException
from products.repository import product_repo
from products.schemas import (
    Product,
    ProductCreate,
    ProductUpdate,
    ProductDetailResponse,
    ProductListResponse,
)


class ProductService:
    def create_product(self, product_req: ProductCreate):
        # 입력받은 데이터(ProductCreate) -> 저장할 객체(Product)로 변환
        new_product = Product(
            name=product_req.name,  # alias 처리되어 name에 들어옴
            price=product_req.price,
            discount_price=product_req.discount_price,
            stock=product_req.stock,
            category=product_req.category,
        )
        saved_product = product_repo.save(new_product)
        # 응답 변환
        return self._to_detail_response(saved_product)

    def get_product(self, product_id: int):
        product = product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
        return self._to_detail_response(product)

    def get_products(self, keyword: str | None, category: str | None, limit: int):
        products = product_repo.get_all(keyword, category, limit)
        # 리스트 컴프리헨션으로 변환
        return [self._to_list_response(p) for p in products]

    def update_product(self, product_id: int, product_req: ProductUpdate):
        product = product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")

        # 데이터 업데이트
        product.name = product_req.name
        product.price = product_req.price
        product.discount_price = product_req.discount_price
        product.stock = product_req.stock
        product.category = product_req.category

        saved_product = product_repo.save(product)
        return self._to_detail_response(saved_product)

    # --- [내부 헬퍼 함수: 응답 변환기] ---
    # 여기서 final_price와 is_sold_out을 계산해서 넣습니다!

    def _to_detail_response(self, product: Product) -> ProductDetailResponse:
        return ProductDetailResponse(
            id=product.id,
            name=product.name,
            category=product.category,
            stock=product.stock,
            final_price=product.price - product.discount_price,  # 최종가 계산
            is_sold_out=product.stock <= 0,  # 품절 여부 계산 (재고가 0 이하면 True)
        )

    def _to_list_response(self, product: Product) -> ProductListResponse:
        return ProductListResponse(
            id=product.id,
            name=product.name,
            category=product.category,
            final_price=product.price - product.discount_price,  # 최종가 계산
        )


product_service = ProductService()
