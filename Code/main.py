import uvicorn
from controller.user import user_app
from controller.car import car_app
from fastapi import Body, FastAPI
from config.app_config import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from common.custom_exception import CustomException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from service.user import signupUser, loginUser
from service.car import addCar,deleteCar,updateCar, showAllCars, showAllAvailableCars, calculatePrice, booking,showBookingCars,showAllBookingCars, approveBooking,disapproveBooking
from sql_app.db import get_db
from fastapi import APIRouter, Depends, Body, UploadFile, File, Query
from model.user import User
from model.car import Car
import json
db = get_db()
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
role = ""

def addCarMethod():
    maker = input("maker: ")
    model = input("model: ")
    year = input("year: ")
    mileage = input("mileage: ")
    minimum_rent_period = input("minimum_rent_period: ")
    maximum_rent_period = input("maximum_rent_period: ")
    unit_price = input("unit_price: ")
    available_now = input("available_now: ")
    addCar(Car(maker=maker, model=model, year=year, mileage=mileage, minimum_rent_period=minimum_rent_period, maximum_rent_period=maximum_rent_period, unit_price=unit_price,available_now=available_now),db)
    print("add car success")
def deleteCarMethod():
    id = input("id: ")
    deleteCar(id,db)
    print("delete car success")
def updateCarMethod():
    id = input("id: ")
    maker = input("maker: ")
    model = input("model: ")
    year = input("year: ")
    mileage = input("mileage: ")
    minimum_rent_period = input("minimum_rent_period: ")
    maximum_rent_period = input("maximum_rent_period: ")
    unit_price = input("unit_price: ")
    available_now = input("available_now: ")
    updateCar(id,Car(maker=maker, model=model, year=year, mileage=mileage, minimum_rent_period=minimum_rent_period, maximum_rent_period=maximum_rent_period, unit_price=unit_price,available_now=available_now),db)
def logoutMethod():
    print("logout success")
    login(db)
def showAllBookingCarsMethod():
    bookingCars = showAllBookingCars(db)
    if(len(bookingCars) == 0):
        print("no booking cars")
    else:
        for car in bookingCars:
            print("car id",car.id)
            print("maker",car.maker)
            print("model",car.model)
            print("year",car.year)
            print("mileage",car.mileage)
            print("minimum_rent_period",car.minimum_rent_period)
            print("maximum_rent_period",car.maximum_rent_period)
            print("unit_price",car.unit_price)
            print("available_now",car.available_now)
            print("---------------------")
def approveMethod():
    showAllBookingCarsMethod()
    id = input("id: ")
    approveBooking(id,db)
    print("approve success")   
def disapproveMethod():
    showAllBookingCarsMethod()
    id = input("id: ")
    disapproveBooking(id,db)
    print("disapprove success") 
def showActions(role):
    if(role == "admin"):
        print("As Admin, please input below actions:showAllAvailableCars,delete, update, add, approve, disapprove, logout")
        action = input("action: ")
        if(action == "delete"):
            deleteCarMethod()
            showActions(role)
        elif (action == "update") :
            updateCarMethod()
            showActions(role)
        elif (action == "add"):
            addCarMethod()
            showActions(role)
        elif (action == "approve"):
            approveMethod()
            showActions(role)
        elif (action == "disapprove"):
            disapproveMethod()
            showActions(role)
        elif (action == "showAllAvailableCars"):
            showAllAvailableCarsMethod()
            showActions(role)
        elif (action == "logout"):
            logoutMethod()
    elif(role == "user"):
        print("As normal user, please input below actions:showAllAvailableCars, calculatePrice, booking, logout")
        action = input("action: ")
        if(action == "calculatePrice"):
            showAllAvailableCarsMethod()
            id = input("id: ")
            rentalDates = int(input("totalRentalDates: "))
            calculatePrice(id,rentalDates,db)
            showActions(role)   
        elif(action == "booking"):
            showAllAvailableCarsMethod()
            id = input("id: ")
            rentalDates = int(input("totalRentalDates: "))
            booking(id,rentalDates,db)
            showActions(role)
        elif(action == "showAllAvailableCars"):
            showAllAvailableCarsMethod()
            showActions(role)
        elif(action == "logout"):
            logoutMethod()
        
def showAllAvailableCarsMethod():
    db = get_db()
    availableCars = showAllAvailableCars(db) 
    for car in availableCars:
        print("car id",car.id)
        print("maker",car.maker)
        print("model",car.model)
        print("year",car.year)
        print("mileage",car.mileage)
        print("minimum_rent_period",car.minimum_rent_period)
        print("maximum_rent_period",car.maximum_rent_period)
        print("unit_price",car.unit_price)
        print("available_now",car.available_now)
        print("---------------------")
def showPage(role):
    print("page",role)
    if(role == "admin"):
        showAllAvailableCarsMethod()
        showActions(role)
    else:
        showAllAvailableCarsMethod()
        showActions(role)

def login (db=Depends(get_db)):
    print("login...")
    account = input("account: ")
    password = input("password: ")
    result = loginUser(User(username=account, password=password),db)
    if(result == "success"):
        if(account == "admin"):
            role = "admin"
            showPage(role)
        else:
            role = "user"
            showPage(role)
        print(f"login success, role is {role}")
    else:
        print("login failed")

def start():
    # global app
    # app.include_router(user_app, prefix='/users', tags=['用户相关API'])
    # app.include_router(car_app, prefix='/cars', tags=['车辆相关API'])
    # uvicorn.run(app, host=APP_HOST, port=APP_PORT)
    print("start and initialing sizing database...")
    signupUser(User(username="admin", password="admin"),db)
    signupUser(User(username="user", password="user"),db)
    #add car
    addCar(Car(maker="Toyota", model="Camry", year=2020, mileage=1000, minimum_rent_period=1, maximum_rent_period=30, unit_price=100,available_now=True),db)
    # addCar(Car(maker="Toyota", model="Corolla", year=2020, mileage=1000, minimum_rent_period=1, maximum_rent_period=30, unit_price=100,available_now=True),db)
    # addCar(Car(maker="Toyota", model="RAV4", year=2020, mileage=1000, minimum_rent_period=1, maximum_rent_period=30, unit_price=100,available_now=True),db)
    print("please register or login your account")
    method = input("method(enter signup or login): ")
    if(method == "signup"):
        print("signup...")
        account = input("account: ")
        password = input("password: ")       
        result = signupUser(User(username=account, password=password),db)
        if(result == "success"):
            print("register success")
            print("please login")
            login(db)
        else:
            print("register failed")
    elif(method == "login"):
        login(db)
    # action = input("action delete update add approve disaprrove logout: ")




if __name__ == '__main__':
    start()
