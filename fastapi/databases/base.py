# # Database Connection Settings
# from sqlalchemy import create_engine, inspect
# from sqlalchemy.schema import CreateSchema
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# from cores.config import settings
# from cores.logger import logger


# p_user = settings.db.POSTGRESQL_USER
# p_password = settings.db.POSTGRESQL_PASSWORD
# p_host = settings.db.POSTGRESQL_HOST
# p_port = settings.db.POSTGRESQL_PORT
# p_database = settings.db.POSTGRESQL_DATABASE
# p_schema = settings.db.POSTGRESQL_SCHEMA

# DATABASE_URL = f"postgresql://{p_user}:{p_password}@{p_host}:{p_port}/{p_database}"
# engine = create_engine(DATABASE_URL, echo=settings.db.echo)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# inspector = inspect(engine)
# if not p_schema in inspector.get_schema_names():
#     logger.info(f"===:=== not found {p_schema}, create schema ===:===")
#     with engine.begin() as conn:
#         conn.execute(CreateSchema(p_schema))

# Base = declarative_base()
# Base.metadata.bind = engine
# Base.metadata.schema = p_schema


# def create_db_and_tables(engine):
#     Base.metadata.create_all(engine)


# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         logger.debug("===:=== db.close() ===:===")
#         db.close()
