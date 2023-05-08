from apis.general_pages.route_homepage import general_pages_router
from fastapi import FastAPI
from core.confing import settings
from fastapi.staticfiles import StaticFiles


def include_router(app):
    app.include_router(general_pages_router) # connect app with ApiRouter(s)

def configure_static(app):  #
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	return app 


app = start_application()


# @app.get("/")
# def hello_api():
#     return {"msg":"Hello Api"}

