import asyncio
from fastapi import APIRouter, Depends, Body, UploadFile, File, Query
from entity.user import User
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
class BaseResponse(BaseModel):
    code: int = Field(200, description="HTTP status code")
    msg: str = Field("success", description="HTTP status message")
    data: Optional[dict]

    class Config:
        schema_extra = {
            "example": {
                "code": 200,
                "msg": "success",
                "data": {
                }
            }
        }
