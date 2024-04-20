# database.py
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:gbs123456@localhost:3306/docnotes_api?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 启动引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# 启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据模型的基类
Base = declarative_base()


def get_session():
    db = SessionLocal()
    return db