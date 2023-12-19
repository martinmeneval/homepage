from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/css", StaticFiles(directory="css"), name="css")
templates = Jinja2Templates("templates")

@app.get("/")
async def render_home(request: Request):
    return templates.TemplateResponse("home.j2", {"request": request})

@app.get("/resume")
async def render_resume(request: Request):
    return templates.TemplateResponse("resume.j2", {"request": request})

@app.get("/li")
async def redirect_li():
    return RedirectResponse("https://www.linkedin.com/in/martin-meneval/")

@app.get("/gh")
async def redirect_gh():
    return RedirectResponse("https://github.com/martinmeneval")

@app.get("/dl_resume")
async def dl_resume():
    return FileResponse("static/resume.pdf",
                     media_type="application/pdf",
                     headers={
                         "Content-Disposition": "attachment; filename=Resume_Martin_Meneval.pdf"
                         }
                     )
