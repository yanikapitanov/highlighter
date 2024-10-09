from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from parser import Parser

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/api/upload")
async def upload(file: UploadFile):
    prs = Parser(file)
    highlights = prs.parse()
    return {"highlights": [highlight for highlight in highlights if highlight is not None]}
