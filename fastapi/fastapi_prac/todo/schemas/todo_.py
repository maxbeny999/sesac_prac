from pydantic import BaseModel, ConfigDict, Field


# [요청] 사용자가 보낼 데이터 (필드명을 content로 통일!)
class TodoCreateRequest(BaseModel):
    content: str = Field(..., min_length=1, max_length=255)


# [응답] 사용자에게 보여줄 데이터
class TodoResponse(BaseModel):
    id: int
    content: str
    is_done: bool

    model_config = ConfigDict(from_attributes=True)
