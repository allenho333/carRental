# models.py
import datetime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Enum,
    DECIMAL,
    DateTime,
    Boolean,
    UniqueConstraint,
    Index,
    func
)
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
# # 基础类
Base = declarative_base()
# print("print(sqlalchemy.__version__)",sqlalchemy.__version__)
# # 创建引擎
# engine = create_engine(
#     # "mysql+pymysql://root:123456gbs@localhost:3306/docnotes_api?charset=utf8mb4",
#     # "mysql+pymysql://scott:tiger@localhost/foo"
#     #  "mysql://{username}:{password}@{server}/testdb"
#     "mysql+pymysql://root:abcd=1234@localhost:3306/carRental",
#     # "mysql+pymysql://tom@127.0.0.1:3306/db1?charset=utf8mb4", # 无密码时
#     # 超过链接池大小外最多创建的链接
#     max_overflow=0,
#     # 链接池大小
#     pool_size=5,
#     # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
#     pool_timeout=10,
#     # 多久之后对链接池中的链接进行一次回收
#     pool_recycle=1,
#     # 查看原生语句（未格式化）
#     echo=True
# )

# # 绑定引擎
# Session = sessionmaker(bind=engine)
# # 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象conn
# # 内部会采用threading.local进行隔离
# session = scoped_session(Session)


# class User(Base):
#     """ 必须继承Base """
#     # 数据库中存储的表名
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(255), unique=True, nullable=False)  # Specify length here
#     password = Column(String(255), nullable=False)

#     __table__args__ = (
#         Index("username", unique=False),  # 姓名索引
#         Index("password", unique=True)  # password索引
#     )

#     def __str__(self):
#         return f"object : <id:{self.id} name:{self.username}>"

# class UserInfo(Base):
#     """ 必须继承Base """
#     # 数据库中存储的表名
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
#     username = Column(String(255), unique=True)
#     phone = Column(String(255), unique=True)
#     hashed_password = Column(String(255))
#     disabled = Column(Boolean, default=False)
#     super = Column(Boolean, default=False)
#     sms_code = Column(String(255), default='')
#     reason = Column(String(255), default='')
#     company = Column(String(255), default='')
#     job = Column(String(255), default='')
#     user_type = Column(String(255), default='')
#     active = Column(String(255), default='active')
#     last_login = Column(DateTime, default=func.now())
#     create_time = Column(DateTime, default=func.now())
#     update_time = Column(DateTime, default=func.now(), onupdate=func.now())

#     __table__args__ = (
#         Index("username", unique=False),  # 姓名索引
#         Index("phone", unique=True)  # 电话索引
#     )

#     def __str__(self):
#         return f"object : <id:{self.id} name:{self.name}>"


# class ModelApi(Base):
#     __tablename__ = "model"
#     id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
#     url = Column(String(256), nullable=False, comment="模型请求地址")
#     available = Column(Boolean(), default=True, comment="服务是否可用")
#     delete_status = Column(Boolean(), default=False,
#                            comment="是否删除(逻辑删除)")
#     create_time = Column(
#         DateTime, default=func.now(), comment="创建时间")


# class UserModel(Base):
#     __tablename__ = "user_model"
#     id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
#     user_id = Column(Integer, nullable=False, comment="用户id")
#     model_id = Column(Integer, nullable=False, comment="模型id")
#     create_time = Column(
#         DateTime, default=func.now(), comment="创建时间")
#     __table__args__ = (
#         UniqueConstraint("user_id", "model_id"),  # 联合唯一约束
#         Index("user_id", unique=False),  # 用户id索引,提高查询该用户下所有模型权限sql的响应速度
#     )


# class File(Base):
#     __tablename__ = "file"
#     id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
#     user_id = Column(Integer, nullable=False, comment="所属用户id")
#     parent_id = Column(Integer, nullable=False, default=0, comment="父级文件id,默认为0代表顶级目录")
#     name = Column(String, nullable=False, unique=True, comment="文件名字")
#     url = Column(String(256), nullable=True, comment="文件存储地址")
#     create_time = Column(
#         DateTime, default=func.now(), comment="创建时间")
#     delete_status = Column(Boolean(), default=False,
#                            comment="是否删除(逻辑删除)")
#     delete_time = Column(DateTime,comment="删除时间")


# class ChatHistory(Base):
#     __tablename__ = "chat_history"
#     id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
#     user_id = Column(Integer, nullable=False, comment="所属用户id")
#     parent_id = Column(Integer, nullable=False, default=0, comment="所属上一条对话记录的id,默认为0代表新会话")
#     role = Column(Enum("human", "assistant"), comment="角色")
#     content = Column(String, comment="对话内容 如果是用户则为query  如果是模型则回复")
#     file_content = Column(String, default="", comment="涉及的文件内容")
#     create_time = Column(
#         DateTime, default=func.now(), comment="创建时间")


# if __name__ == "__main__":
#     # 删除表
#     Base.metadata.drop_all(engine)
#     # 创建表
#     Base.metadata.create_all(engine)
