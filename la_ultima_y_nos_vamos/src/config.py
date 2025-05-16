# Configuration loader.

import os

class Config:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///default.db")
        self.secret_key = os.getenv("SECRET_KEY", "default_secret_key")
        self.debug = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

    def load(self):
        return {
            "database_url": self.database_url,
            "secret_key": self.secret_key,
            "debug": self.debug,
        }