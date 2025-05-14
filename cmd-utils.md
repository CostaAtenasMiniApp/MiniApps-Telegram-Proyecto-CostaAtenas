## Para ejecutar el bot student
python -m src.bots.bot_student.main

## Para ejecutar la miniapp
python -m src.miniapps.main

## Mini servidor http para test html
python -m http.server

## Migrar la BD

aerich init -t src.infrastructure.database.tortoise_db_models.init_db.TORTOISE_ORM
aerich init-db

aerich migrate --name initial  # Crea la migración
aerich upgrade  # Aplica los cambios a la BD

### Web Hoock

# Desplegar el webhook
$token = "7530043961:AAGaRMdy23ibreyLqSJzUcf9IIssPNZsAlg"
$webhookUrl = "https://telegram-bot-scheduler.yosbel-penate.workers.dev/"
Invoke-RestMethod -Uri "https://api.telegram.org/bot$($token)/setWebhook?url=$($webhookUrl)" -Method Post

# Verificar Usa ESTE formato (nota el /bot antes del token):
$token = "7530043961:AAGaRMdy23ibreyLqSJzUcf9IIssPNZsAlg"
$response = Invoke-RestMethod "https://api.telegram.org/bot$token/getWebhookInfo"
$response.result.url

