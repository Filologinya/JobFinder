from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates # template front


templates = Jinja2Templates(directory="templates") # create an object J2T
general_pages_router = APIRouter() #mini FastAPI apps

@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})