from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, DateTime
from app.database import Base
from datetime import datetime

# Модель алхимии - модель поста
class Posts(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime] 

    