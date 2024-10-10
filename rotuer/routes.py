from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from persistence.database import create_db_and_tables, SessionDep
from logic import save_highlights

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/api/upload")
async def upload(file: UploadFile, session: SessionDep):
    highlights = save_highlights(session, file)
    return {"highlights": highlights}
