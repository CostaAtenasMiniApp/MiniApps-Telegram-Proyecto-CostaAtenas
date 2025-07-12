from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.infrastructure.routes.web_page import router as api_router
from src.shared import config

def create_app() -> FastAPI:
    """
    Función de fábrica para crear y configurar la aplicación FastAPI.
    """
    # 1. Crear la instancia de la aplicación
    app = FastAPI(
        title="Proyecto Costa Atenas",
        description="API para la gestión de la MiniApp de Telegram.",
        version="1.0.0"
    )


    # 3. Montar el directorio de archivos estáticos
    #    Esto permite que FastAPI sirva archivos como CSS, JS, etc.
    app.mount(
        "/static",
        StaticFiles(directory=config.STATIC_DIR),
        name="static"
    )
    # 4. Incluir las rutas de la aplicación
    #    Esto registra todos los endpoints definidos en src/apps/routes.py
    app.include_router(api_router, prefix="")
    # 5. Devolver la aplicación configurada
    return app