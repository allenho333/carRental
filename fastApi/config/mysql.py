# 1.导入 SQLAlchemy 部件
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 2.为 SQLAlchemy 定义数据库 URL地址
DATABASE_URL = "postgresql://rds_db_testpg:DocnotesV1@postgresql15.rdsg4beop507koc.rds.bj.baidubce.com:3306/docnotes_test"

# 3.创建 SQLAlchemy 引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# 4.创建一个SessionLocal 用于给每个请求创建数据库会话  相当于数据库连接池
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5.创建一个Base类  用于ORM映射
Base = declarative_base()