from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.infrastructure.routes import web_page
import src.shared.config
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")
app.include_router(web_page.router, prefix="")

def start_fastapi_server():
    uvicorn.run(app, host="127.0.0.1", port=3000, log_level="info")
