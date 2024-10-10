from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Field, SQLModel, Session


class HighlightEntity(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author: str = Field(index=True)
    title: str = Field(index=True)
    content: str = Field(index=False)


postgres_url = "postgresql://myuser:mypassword@localhost:5432/dbs_highlighter"
engine = create_engine(postgres_url, echo=True, future=True)

def create_db_and_tables():
    SQLModel.metadata.schema = "scm_highlighter"
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
