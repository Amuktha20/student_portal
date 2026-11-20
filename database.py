from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine(
    "sqlite:///./users.db"
    
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=True,
    autocommit=False
)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()