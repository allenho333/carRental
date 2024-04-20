import asyncio
from fastapi import APIRouter, Depends, Body, UploadFile, File, Query
from model.user import User
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from service.user import signupUser
from model.baseResponse import BaseResponse
user_app = APIRouter()
from sql_app.db import get_db

# class BaseResponse(BaseModel):
#     code: int = Field(200, description="HTTP status code")
#     msg: str = Field("success", description="HTTP status message")
#     data: Optional[dict]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "code": 200,
#                 "msg": "success",
#                 "data": {
#                 }
#             }
#         }
# @user_app.post("/login")
# async def user_login(user: UserCreate):
#     print("用户登录")
#     return BaseResponse( code=200,
#                     msg=f'login in success', 
#                     data={
#                         "data":"data"
#                     })
@user_app.post("/signup")
async def user_signup(user: User, db=Depends(get_db)):
    return signupUser(user,db)

@user_app.post("/login")
async def user_login(user: User, db=Depends(get_db)):
    return loginUser(user,db)
# user_app.post('/login')(user_login)
# user_app.get('/profile')(user_profile)
