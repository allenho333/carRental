from sql_app import user_sql_app
from common.custom_exception import CustomException
from common.error_enum import Error
from model.baseResponse import BaseResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from sql_app.db import get_db
from sql_app.models import User
def signupUser(user: User, db: Session):
    # 检查用户名合法性
    # if user.username == "" or user_sql_app.select_user_by_name(user.username) is not None:
    #     # 用户名不合法抛出异常
    #     # raise CustomException.init(Error.USER_CREATE_PARAMETER_ERROR)
    #     return BaseResponse( code=400,
    #                 msg=f'create user failed', 
    #                 data={
    #                     "data":"datafail"
    #                 })
    # print("已成功注册用户")
    print("user.username",user.username)
    print("user.password",user.password)
    user_instance = User(username=user.username, password=user.password)
    print("user_instance",user_instance)
    db.add(user_instance)
    print("going to db.commit()")
    db.commit()
    db.refresh(user_instance)
    return BaseResponse( code=200,
                    msg=f'create user success', 
                    data={
                        "data":"create user success"
                    })


def loginUser(user: User, db: Session):
    # # 检查用户名合法性
    # if user.username == "" or user_sql_app.select_user_by_name(user.username) is None:
    #     # 用户名不合法抛出异常
    #     raise CustomException.init(Error.USER_LOGIN_PARAMETER_ERROR)
    print("已成功登录用户")
    return BaseResponse( code=200,
                    msg=f'login in success', 
                    data={
                        "data":"data"
                    })

