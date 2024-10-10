from typing import List

from fastapi import UploadFile
from sqlmodel import Session

from model.models import Highlight
from parser import Parser
from persistence.database import HighlightEntity


def save_highlights(session: Session, file: UploadFile) -> List[Highlight]:
    highlights = Parser(file).parse()
    entities = [HighlightEntity(title=highlight.title, author=highlight.author, content=highlight.content) for highlight in highlights if highlight is not None and highlight.content is not None]
    [session.add(entity) for entity in entities]
    session.commit()
    return highlights
