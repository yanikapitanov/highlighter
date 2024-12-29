from typing import Annotated, List

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Field, SQLModel, Session


class HighlightEntity(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author: str = Field(index=True)
    title: str = Field(index=True)
    content: str = Field(index=False)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
