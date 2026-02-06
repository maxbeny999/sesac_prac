from fastapi import APIRouter, status
from products.schemas.category import CategoryCreate, CategoryRead
from products.service.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=CategoryRead)
def create_category(cat: CategoryCreate):
    return service.create_category(cat)


@router.get("", response_model=list[CategoryRead])
def get_categories():
    return service.get_categories()
