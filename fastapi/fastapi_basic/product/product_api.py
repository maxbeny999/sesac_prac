# fastapi_basic/product/product_api.py

from fastapi import APIRouter

# 같은 폴더(.product)에 있는 product.py에서 클래스 가져오기
from .product import ProductCreate, Product

# 주소 접두사 설정: /products
router = APIRouter(prefix="/products")

# 상품 데이터를 저장할 리스트
products = []


# 1. 상품 등록 (POST)
@router.post("")
def create_product(product_data: ProductCreate):
    # 사용자가 보낸 id, 이름, 가격을 그대로 사용하여 객체 생성
    new_product = Product(
        product_data.id, product_data.product_name, product_data.price
    )

    products.append(new_product)

    return new_product


# 2. 전체 조회 (GET)
@router.get("")
def read_products():
    return products


# 3. 단일 조회 (GET /{id})
@router.get("/{id}")
def read_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "상품을 찾을 수 없습니다."}


# 4. 삭제 (DELETE /{id}) - (필요시 사용)
@router.delete("/{id}")
def delete_product(id: int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return {"message": "삭제되었습니다."}
    return {"message": "상품을 찾을 수 없습니다."}
