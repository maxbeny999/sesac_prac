from pydantic import BaseModel, Field
from datetime import datetime


class ReviewCreate(BaseModel):
    reservation_id: int
    rating: int = Field(..., ge=1, le=5, description="평점 (1~5)")
    comment: str


class ReviewResponse(ReviewCreate):
    id: int
    user_id: int
    created_at: datetime

    model_config = {"from_attributes": True}
