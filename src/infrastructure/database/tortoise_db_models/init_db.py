from tortoise import Tortoise, run_async
from .models import initialize_discovery_methods

# Configuración necesaria para Aerich (añade esto)
TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": [
                "src.infrastructure.database.tortoise_db_models.models",
                "aerich.models"  # ¡Importante para Aerich!
            ],
            "default_connection": "default",
        },
    },
}

async def init_db():
    # Usa la configuración de TORTOISE_ORM
    await Tortoise.init(config=TORTOISE_ORM)  # <- Cambia esta línea
    await Tortoise.generate_schemas()
    await initialize_discovery_methods()
    print("✅ Base de datos SQLite inicializada")

# (El resto del código se mantiene igual)