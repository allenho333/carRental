import uvicorn
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
    booking_now = input("booking_now: ")
    addCar(Car(maker=maker, model=model, year=year, mileage=mileage, minimum_rent_period=minimum_rent_period, maximum_rent_period=maximum_rent_period, unit_price=unit_price,available_now=available_now,
    booking_now = booking_now
    ),db)
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
    booking_now = input("booking_now: ")
    updateCar(id,Car(maker=maker, model=model, year=year, mileage=mileage, minimum_rent_period=minimum_rent_period, maximum_rent_period=maximum_rent_period, unit_price=unit_price,available_now=available_now,booking_now = booking_now),db)
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
        print("As Admin, please input below actions number: \n 1: showAllAvailableCars, \n 2: delete, \n 3:update, \n 4:add, \n 5: approve, \n 6:disapprove, \n7: logout")
        while True:
            action = input("action number: ")
            if(action == "2"):
                deleteCarMethod()
                showActions(role)
            elif (action == "3") :
                updateCarMethod()
                showActions(role)
            elif (action == "4"):
                addCarMethod()
                showActions(role)
            elif (action == "5"):
                approveMethod()
                showActions(role)
            elif (action == "6"):
                disapproveMethod()
                showActions(role)
            elif (action == "1"):
                showAllAvailableCarsMethod()
                showActions(role)
            elif (action == "7"):
                logoutMethod()
    elif(role == "user"):
        print("As normal user, please input below actions: \n 1: showAllAvailableCars, \n 2:calculatePrice, \n 3:booking,\n 4: logout")
        while True:
            action = input("action number: ")
            if(action == "2"):
                showAllAvailableCarsMethod()
                id = input("id: ")
                rentalDates = int(input("totalRentalDates: "))
                calculatePrice(id,rentalDates,db)
                showActions(role)   
            elif(action == "3"):
                showAllAvailableCarsMethod()
                id = input("id: ")
                rentalDates = int(input("totalRentalDates: "))
                booking(id,rentalDates,db)
                showActions(role)
            elif(action == "1"):
                showAllAvailableCarsMethod()
                showActions(role)
            elif(action == "4"):
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
    while True:
        print("login...")
        account = input("account: ")
        password = input("password: ")
        result = loginUser(User(username=account, password=password),db)
        print("result",result)
        if(result == "success"):
            if(account == "admin"):
                role = "admin"
                print(f"login success, role is {role}")
                showPage(role)
            else:
                role = "user"
                print(f"login success, role is {role}")
                showPage(role)
            
        else:
            print("login failed, please try again")
            # login(db)
def initializeDatabse():
    print("initialing database and add sample data...")
    # add admin user with username as admin and password as admin to database
    signupUser(User(username="admin", password="admin"),db)
    print("add admin user with username as admin and password as admin t o database")
    # add normal user with username as user and password as user to database
    signupUser(User(username="user", password="user"),db)
    print("add normal user with username as user and password as user to database")
    #add cars
    addCar(Car(maker="Toyota", model="Camry", year=2020, mileage=1000, minimum_rent_period=1, maximum_rent_period=30, unit_price=100,available_now=True,
    booking_now = False),db)
    addCar(Car(maker="Toyota", model="Corolla", year=2020, mileage=1000, minimum_rent_period=1, maximum_rent_period=30, unit_price=100,available_now=True,booking_now = False),db)
    addCar(Car(maker="Toyota", model="RAV4", year=2020, mileage=1000, minimum_rent_period=1, maximum_rent_period=30, unit_price=100,available_now=True,booking_now = False),db)

def start():
    initializeDatabse()
    while True:
        print("please signup or login your account: \n 1. signup \n 2. login")
        method = input("method(enter 1 for signup or 2 for login): ")
        if(method == "1"):
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
        elif(method == "2"):
            login(db)
   
if __name__ == '__main__':
    start()
