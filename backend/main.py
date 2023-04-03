from fastapi import FastAPI
from core.confing import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"msg":"Hello Api"}

