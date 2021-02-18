from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


from .short_url import ShortURL

api = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Ephemeral storage
SHORT = ShortURL()


@api.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Hello World"})


# Route for the redirection from shorturl to long url
@api.get("/{short_url}")
def short_to_long(short_url: str):
    long = SHORT.get(short_url)
    if long is not None:
        return RedirectResponse(long)
    return RedirectResponse("/")


# Route for creating a short url form a long url
@api.post("/")
def long_to_short(long_url: str = Form(...)):
    return {"short_url": SHORT.add(long_url)}
