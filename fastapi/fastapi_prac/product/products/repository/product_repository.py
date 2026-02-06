from sqlmodel import Session, select
from connection import engine
from products.models import Product, Category


class ProductRepository:
    def save(self, product: Product) -> Product:
        with Session(engine) as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            return product

    def get_by_id(self, product_id: int) -> Product | None:
        with Session(engine) as session:
            return session.get(Product, product_id)

    def get_all(
        self, keyword: str | None, category_name: str | None, limit: int
    ) -> list[Product]:
        with Session(engine) as session:
            query = select(Product)

            if category_name:
                query = query.join(Category).where(Category.name == category_name)

            if keyword:
                query = query.where(Product.name.contains(keyword))

            query = query.limit(limit)
            return list(session.exec(query).all())
