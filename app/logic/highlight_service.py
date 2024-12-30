from typing import List

from asyncpg import DuplicateObjectError
from fastapi import UploadFile
from sqlmodel import Session

from app.logic.parser import Parser
from app.model.models import Highlight
from app.persistence.database import HighlightEntity


def save_highlights(session: Session, file: UploadFile) -> List[Highlight]:
    highlights = Parser(file).parse()
    entities = [HighlightEntity(title=highlight.title, author=highlight.author, content=highlight.content, hash=hash(highlight)) for highlight
                in highlights if highlight is not None and highlight.content is not None and find_by_hash(session, highlight) is None]

    [session.add(entity) for entity in entities]
    session.commit()
    return highlights


def find_by_hash(session: Session, highlight: Highlight) -> Highlight:
    return session.query(HighlightEntity).filter(HighlightEntity.hash == hash(highlight)).first()

def save(session: Session, highlight: Highlight) -> Highlight:
    entity = HighlightEntity(title=highlight.title, author=highlight.author, content=highlight.content, hash=hash(highlight))
    if find_by_hash(session, highlight) is not None:
        raise DuplicateObjectError()
    session.add(entity)
    session.commit()
    return highlight


def fetch_all(session: Session) -> List[Highlight]:
    all_entities = session.query(HighlightEntity).all()
    return [Highlight(title=e.title, author=e.author, content=e.content) for e in all_entities]
