from typing import Optional
from fastapi import APIRouter

router = APIRouter(prefix="/auth")


@router.get("/")
def index():
    return {"message": "hello world, tigers team"}


@router.get("/option/")
def optional(option: Optional[str] = None):
    return {"option": option}


@router.get("/post/{post_id}")
def one(post_id: int):
    return {"post_id": post_id}
