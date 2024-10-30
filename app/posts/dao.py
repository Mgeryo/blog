from datetime import datetime
from app.database import async_session_maker
from sqlalchemy import delete, insert, select, update
from app.posts.models import Posts


class DAO:
    # модель алхимии
    model = Posts
    
    # находит одну запись в бд, удовлетворяющую условиям
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    # находит все записи в бд, удовлетворяющие условиям
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    # обновляем запись в бд
    @classmethod
    async def update_post(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()
        
    # добавляет запись в блог
    @classmethod 
    async def add(
        cls,
        title: str,
        content: str,
    ):
        async with async_session_maker() as session:
            add_post = insert(cls.model).values(
                    title=title,
                    content=content,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            await session.execute(add_post)
            await session.commit()
    
    @classmethod 
    async def update(
        cls,
        id: int,
        title: str,
        content: str,
    ):
        async with async_session_maker() as session:
            post = update(cls.model).where(cls.model.id==id).values(
                title=title,
                content=content,
                updated_at=datetime.now(),
            )
            await session.execute(post)
            await session.commit()        

    # удаляет запись из бд
    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()