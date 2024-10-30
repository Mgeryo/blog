from datetime import datetime
from fastapi import APIRouter

from app.posts.dao import DAO
from app.posts.schemas import SNewpost, Spost

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("")
async def get_all_posts(
    )-> list[Spost]:
    posts = await DAO.find_all()
    return posts

@router.get("/{id}")
async def get_post_by_id(
    id: int
    )-> Spost:
    post_by_id = await DAO.find_one_or_none(id = id)
    return post_by_id

@router.post("")
async def create_new_post(
    post: SNewpost
    ):
    new_post = await DAO.add(
        post.title,
        post.content,
    )

@router.put("/{id}")
async def update_post(
    id: int,
    post: SNewpost
):
    await DAO.update(
        id, 
        post.title, 
        post.content
    )
    
@router.delete("/{id}")
async def remove_post(
    id: int
    ):
     await DAO.delete(id=id)

