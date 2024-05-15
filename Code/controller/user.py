# import asyncio
# from fastapi import APIRouter, Depends, Body, UploadFile, File, Query
# from model.user import User
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, Field
# from typing import Optional
# from service.user import signupUser, loginUser
# from service.car import addCar
# from model.baseResponse import BaseResponse
# from sql_app.db import get_db
# user_app = APIRouter()
# @user_app.post("/signup")
# async def user_signup(user: User, db=Depends(get_db)):
#     return signupUser(user,db)

# @user_app.post("/login")
# async def user_login(user: User, db=Depends(get_db)):
#     return loginUser(user,db)

# # user_app.post('/login')(user_login)
# # user_app.get('/profile')(user_profile)
