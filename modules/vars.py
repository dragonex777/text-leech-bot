import os

API_ID    = os.environ.get("API_ID", "24515547")
API_HASH  = os.environ.get("API_HASH", "0809699a061f02fbbcc1a6c4443547ee")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8138754480:AAHZKerxsZdMO68gWw3HdEYTIimlTlzwMr8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
