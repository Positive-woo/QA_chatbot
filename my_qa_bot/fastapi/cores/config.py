import os


class Server:
    def __init__(self):
        self.is_production = os.environ.get("is_production").lower() == "true"
        self.log_level = os.environ.get("log_level", "WARNING")
        self.cors_allow_credentials = os.environ.get("cors_allow_credentials")
        self.cors_allow_methods = os.environ.get("cors_allow_methods")
        self.cors_allow_headers = os.environ.get("cors_allow_headers")
        self.cors_allow_origins = os.environ.get("cors_allow_origins")
        self.volume_dir = os.environ.get("volume_dir", "volume")
        self.log_dir = os.environ.get("log_dir", "log")


# class Database:
#     def __init__(self):
#         self.echo = os.environ.get("echo").lower() == "true"
#         # Postgresql
#         self.POSTGRESQL_USER = os.environ.get("POSTGRESQL_USER")
#         self.POSTGRESQL_PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
#         self.POSTGRESQL_HOST = os.environ.get("POSTGRESQL_HOST")
#         self.POSTGRESQL_PORT = os.environ.get("POSTGRESQL_PORT")
#         self.POSTGRESQL_DATABASE = os.environ.get("POSTGRESQL_DATABASE")
#         self.POSTGRESQL_SCHEMA = os.environ.get("POSTGRESQL_SCHEMA")
#         # Redis
#         self.REDIS_HOST = os.environ.get("REDIS_HOST")
#         self.REDIS_PORT = os.environ.get("REDIS_PORT")
#         self.REDIS_DATABASE = os.environ.get("REDIS_DATABASE")
#         self.REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")


# class Security:
#     def __init__(self):
#         self.secret_key = os.environ.get("SECRET_KEY")
#         self.refresh_secret_key = os.environ.get("REFRESH_SECRET_KEY")
#         self.algorithm = os.environ.get("ALGORITHM")
#         self.access_token_expire_minutes = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
#         self.refresh_token_expire_days = os.environ.get("REFRESH_TOKEN_EXPIRE_DAYS")


class Settings:
    def __init__(self):
        self.server = Server()
        # self.db = Database()
        # self.security = Security()

    def get(self, path, default=None):
        parts = path.split(".")
        current = self
        for part in parts:
            if hasattr(current, part):
                current = getattr(current, part)
            else:
                return default
        return current


settings = Settings()
