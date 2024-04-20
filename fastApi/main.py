import uvicorn
from controller.user import user_app
from fastapi import Body, FastAPI
from config.app_config import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from common.custom_exception import CustomException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]  # Replace with your allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,  # Set to True if cookies are involved
    allow_methods=["*"],  # List of allowed HTTP methods (e.g., GET, POST, PUT)
    allow_headers=["*"],  # List of allowed request headers
)

# 全局自定义异常捕获器
@app.exception_handler(CustomException)
async def handler_custom_exception(error: CustomException):
    return JSONResponse(
        status_code=error.code,
        content=error.message,
    )


async def document():
    return RedirectResponse(url="/docs")


def start():
    global app
    app.include_router(user_app, prefix='/users', tags=['用户相关API'])
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)


if __name__ == '__main__':
    start()
