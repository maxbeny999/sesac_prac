from sqlmodel import Session, select
from connection import engine
from products.models import Category


class CategoryRepository:
    def save(self, category: Category) -> Category:
        with Session(engine) as session:
            session.add(category)
            session.commit()
            session.refresh(category)
            return category

    def get_by_name(self, name: str) -> Category | None:
        with Session(engine) as session:
            statement = select(Category).where(Category.name == name)
            return session.exec(statement).first()

    def get_all(self) -> list[Category]:
        with Session(engine) as session:
            return list(session.exec(select(Category)).all())

    def get_by_id(self, category_id: int) -> Category | None:
        with Session(engine) as session:
            return session.get(Category, category_id)
