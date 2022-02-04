from typing import Optional

from sqlmodel import Field, SQLModel


class PostBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)


class PostCreate(PostBase):
    pass
