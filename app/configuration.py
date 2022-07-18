import os
import logging
from dotenv import load_dotenv
logger=logging.getLogger(__name__)

load_dotenv("env")

class Settings:
    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")


setting = Settings()