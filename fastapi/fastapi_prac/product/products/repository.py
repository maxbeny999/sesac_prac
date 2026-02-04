# products/repository.py
from sqlmodel import Session, select
from connection import engine
from products.schemas import Product


class ProductRepository:
    def save(self, product: Product):
        with Session(engine) as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            return product

    def get_by_id(self, product_id: int):
        with Session(engine) as session:
            return session.get(Product, product_id)

    # 검색과 필터링 로직
    def get_all(self, keyword: str | None, category: str | None, limit: int):
        with Session(engine) as session:
            query = select(Product)

            # 검색어가 있으면 (SQL의 WHERE name LIKE '%keyword%')
            if keyword:
                query = query.where(Product.name.contains(keyword))

            # 카테고리가 있으면
            if category:
                query = query.where(Product.category == category)

            # 개수 제한
            query = query.limit(limit)

            return session.exec(query).all()


product_repo = ProductRepository()
