from src.infrastructure.database.tortoise_db_models.models.DiscoveryMethod import DiscoveryMethod
from src.infrastructure.database.tortoise_db_models.models.initial_data import DISCOVERY_METHODS_DATA

from tortoise.exceptions import IntegrityError
import logging


logger = logging.getLogger(__name__)

async def initialize_discovery_methods():
    try:
        for method_data in DISCOVERY_METHODS_DATA:
            try:
                await DiscoveryMethod.get_or_create(
                    name=method_data["name"],
                    defaults={
                        "category": method_data["category"],
                        "icon": method_data["icon"]
                    }
                )
            except IntegrityError:
                logger.warning(f"El método {method_data['name']} ya existe")
            except Exception as e:
                logger.error(f"Error al crear {method_data['name']}: {str(e)}")

        logger.info("Métodos de descubrimiento inicializados correctamente")
    except Exception as e:
        logger.error(f"Error en initialize_discovery_methods: {str(e)}")
        raise