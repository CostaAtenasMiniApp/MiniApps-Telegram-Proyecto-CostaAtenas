# Comandos

## Para ejecutar el bot student

```sh
python -m src.bots.bot_student.main
```

## Para ejecutar la miniapp

```sh
python -m src.apps.main
```

## Ejecutar la nueva web

```sh
uvicorn src.infrastructure.fastapi_server:app --reload --port 8000
```

## Mini servidor http para test html

```sh
python -m http.server
```

## Migrar la BD

# 1. Inicializa Aerich (solo primera vez)
aerich init -t src.infrastructure.database.tortoise_db_models.init_db.TORTOISE_ORM

# 2. Crea la migración inicial
aerich init-db

# 3. Genera las migraciones (si hay cambios)
aerich migrate --name "initial_migration"

# 4. Aplica migraciones
aerich upgrade

### Web Hoock

# Desplegar el webhook
$token = "7530043961:AAGaRMdy23ibreyLqSJzUcf9IIssPNZsAlg"
$webhookUrl = "https://telegram-bot-scheduler.yosbel-penate.workers.dev/"
Invoke-RestMethod -Uri "https://api.telegram.org/bot$($token)/setWebhook?url=$($webhookUrl)" -Method Post

# Verificar Usa ESTE formato (nota el /bot antes del token):
$token = "7530043961:AAGaRMdy23ibreyLqSJzUcf9IIssPNZsAlg"
$response = Invoke-RestMethod "https://api.telegram.org/bot$token/getWebhookInfo"
$response.result.url

