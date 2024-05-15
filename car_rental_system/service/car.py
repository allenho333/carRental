# addCar
from sql_app import user_sql_app
from common.custom_exception import CustomException
from common.error_enum import Error
from model.baseResponse import BaseResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from sql_app.db import get_db
from config.database import Car

def addCar(car: Car, db: Session):
    car_instance = Car(
        maker=car.maker,
        model=car.model,
        year=car.year,
        mileage=car.mileage,
        minimum_rent_period=car.minimum_rent_period,
        maximum_rent_period=car.maximum_rent_period,
        unit_price=car.unit_price
    )
    db.add(car_instance)
    db.commit()
    db.refresh(car_instance)
    print("add car success")

def deleteCar(id: int, db: Session):
    car_instance = db.query(Car).filter(Car.id == id).first()
    db.delete(car_instance)
    db.commit()
    print("delete car success")

def updateCar(id:int, car: Car, db: Session):
    car_instance = db.query(Car).filter(Car.id == id).first()
    if(car_instance is None):
        print("update car fail, car not found")
        return
    car_instance.maker = car.maker
    car_instance.model = car.model
    car_instance.year = car.year
    car_instance.mileage = car.mileage
    car_instance.available_now = car.available_now
    car_instance.minimum_rent_period = car.minimum_rent_period
    car_instance.maximum_rent_period = car.maximum_rent_period
    car_instance.unit_price = car.unit_price
    car_instance.booking_now = car.booking_now
    db.commit()
    db.refresh(car_instance)
    print("update car success")
    
def showAllCars(db: Session):
    car_instance = db.query(Car).all()
    return car_instance
    
def showAllBookingCars(db: Session):
    car_instance = db.query(Car).filter(Car.booking_now == True).all()
    return car_instance
   
def showAllAvailableCars(db: Session):
    car_instance = db.query(Car).filter(Car.available_now == True).all()
    return car_instance
    

def calculatePrice(id: int, rentalDates:int, db: Session):
    car_instance = db.query(Car).filter(Car.id == id).first()
    result = car_instance.unit_price * rentalDates
    print("unit price:",car_instance.unit_price)
    print("rental dates:",rentalDates)
    print("calculate price success:",result)
    


def booking(id: int, rentalDates:int, db: Session):
    car_instance = db.query(Car).filter(Car.id == id).first()
    car_instance.booking_now = True
    car_instance.available_now = False
    db.commit()
    print("booking success")
    

def showBookingCars(db: Session):
    car_instance = db.query(Car).filter(Car.booking_now == True).all()
    return car_instance
    
def approveBooking(id: int, db: Session):
    car_instance = db.query(Car).filter(Car.id == id).first()
    if car_instance is not None :
        car_instance.booking_now = False
        car_instance.available_now = False
        db.commit()
    print("approve booking success")
   
def disapproveBooking(id: int, db: Session):
    car_instance = db.query(Car).filter(Car.id == id).first()
    if car_instance is not None :
        car_instance.booking_now = False
        car_instance.available_now = True
        db.commit()
    print("disapprove booking success")
    

