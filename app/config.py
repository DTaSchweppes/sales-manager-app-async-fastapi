from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/postgres"# +asyncpg
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(autocommit= False, autoflush =False, bind=engine)
Base = declarative_base()

