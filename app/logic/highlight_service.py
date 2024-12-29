from typing import List

from fastapi import UploadFile
from sqlmodel import Session

from app.model.models import Highlight
from app.logic.parser import Parser
from app.persistence.database import HighlightEntity


def save_highlights(session: Session, file: UploadFile) -> List[Highlight]:
    highlights = Parser(file).parse()
    entities = [HighlightEntity(title=highlight.title, author=highlight.author, content=highlight.content) for highlight in highlights if highlight is not None and highlight.content is not None]
    [session.add(entity) for entity in entities]
    session.commit()
    return highlights

def fetch_all(session: Session) -> List[Highlight]:
    return session.query(HighlightEntity).all()