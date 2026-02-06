from fastapi import HTTPException
from products.repository.category_repository import CategoryRepository
from products.models import Category
from products.schemas.category import CategoryCreate


class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def create_category(self, cat_req: CategoryCreate):
        if self.repo.get_by_name(cat_req.name):
            raise HTTPException(status_code=400, detail="이미 존재하는 카테고리입니다.")

        new_cat = Category(name=cat_req.name)
        return self.repo.save(new_cat)

    def get_categories(self):
        return self.repo.get_all()
