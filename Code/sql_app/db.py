from config.database import SessionLocal


def get_db():
    db = SessionLocal()
    return db
