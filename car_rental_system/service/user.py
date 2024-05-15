from sql_app import user_sql_app
from common.custom_exception import CustomException
from common.error_enum import Error
from model.baseResponse import BaseResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from sql_app.db import get_db
from config.database import User
def signupUser(user: User, db: Session):
    if user.username == "" or user_sql_app.select_user_by_name(user.username) is not None:
        return "fail, user already existed or username is empty"
    print("signup fail")
    user_instance = User(username=user.username, password=user.password)
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return "success"


def loginUser(user: User, db: Session):
    if user.username == "" or user_sql_app.select_user_by_name(user.username) is None or user.password == "" or user_sql_app.select_user_by_name(user.username).password != user.password:
        return "fail"
    print("login success")
    return "success"

