import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
BASE_DIR = os.path.join(ROOT_DIR, "src")

DB_DIR = os.path.join(ROOT_DIR, "database.db")
STATIC_DIR = os.path.join(BASE_DIR, "adapters", "web_ui", "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "adapters", "web_ui", "templates")