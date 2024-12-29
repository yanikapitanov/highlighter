from fastapi import APIRouter, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.logic.highlight_service import save_highlights, fetch_all
from app.persistence.database import create_db_and_tables, SessionDep

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.on_event("startup")
def on_startup():
    create_db_and_tables()


@router.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@router.post("/api/highlight")
async def upload(file: UploadFile, session: SessionDep):
    highlights = save_highlights(session, file)
    return {"highlights": highlights}


@router.get("/api/highlight")
async def fetch(session: SessionDep):
    highlights = fetch_all(session)
    return {"highlights": highlights}
