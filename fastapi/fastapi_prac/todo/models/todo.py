from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from database import Base


class Todo(Base):
    __tablename__ = "todos"  # DB에 생성될 테이블 이름

    # Mapped[...]는 SQLAlchemy 2.0의 최신 문법입니다.
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
