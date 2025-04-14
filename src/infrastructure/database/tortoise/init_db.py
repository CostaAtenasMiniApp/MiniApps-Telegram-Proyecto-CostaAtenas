from tortoise import Tortoise, run_async

async def init_db():
    # Configuración de la conexión a SQLite
    await Tortoise.init(
        db_url = "sqlite://db.sqlite3",  # Ruta al archivo SQLite
        modules={
            "models": [
                "src.infrastructure.database.tortoise.models",  # Ruta a tus modelos
            ]
        }
    )

    # Genera los esquemas en la base de datos solo si no están creados
    await Tortoise.generate_schemas()
    print("✅ Base de datos SQLite inicializada")

# Ejecutar la inicialización (solo para pruebas)
""" if __name__ == "__main__":
    run_async(init_db()) """