# import asyncio
# from fastapi import APIRouter, Depends, Body, UploadFile, File, Query
# from model.car import Car
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, Field
# from typing import Optional
# from service.user import signupUser, loginUser
# from service.car import addCar,deleteCar,updateCar, showAllAvailableCars, calculatePrice, booking,showBookingCars,showAllCars, approveBooking,disapproveBooking,showAllBookingCars
# from model.baseResponse import BaseResponse
# from sql_app.db import get_db
# car_app = APIRouter()


# @car_app.post("/add")
# async def car_add(car: Car, db=Depends(get_db)):
#     return addCar(car,db)
# #delete
# @car_app.delete("/delete")
# async def car_delete(id: int, db=Depends(get_db)):
#     return deleteCar(id,db)
# #update
# @car_app.put("/update")
# async def car_update(id: int,car: Car, db=Depends(get_db)):
#     return updateCar(id,car,db)

# #showAllCars
# @car_app.get("/showAllCars")
# async def car_showAllCars(db=Depends(get_db)):
#     return showAllCars(db)
# #showAllAvailableCars
# @car_app.get("/showAllAvailableCars")
# async def car_showAllAvailableCars(db=Depends(get_db)):
#     return showAllAvailableCars(db)

# # calculate price
# @car_app.get("/calculatePrice")
# async def car_calculatePrice(id: int, rentalDates:int, db=Depends(get_db)):
#     return calculatePrice(id,rentalDates,db)

# # booking
# @car_app.get("/booking")
# async def car_booking(id: int, rentalDates:int, db=Depends(get_db)):
#     return booking(id,rentalDates,db)
# #showAllBookingCars
# @car_app.get("/showAllBookingCars")
# async def car_showAllBookingCars(db=Depends(get_db)):
#     return showAllBookingCars(db)
# #showBookingCars
# @car_app.get("/showBookingCars")
# async def car_showBookingCars(db=Depends(get_db)):
#     return showBookingCars(db)

# @car_app.get("/approveBooking")
# async def car_approveBooking(id: int, db=Depends(get_db)):
#     return approveBooking(id,db)

# @car_app.get("/rejectBooking")
# async def car_rejectBooking(id: int, db=Depends(get_db)):
#     return disapproveBooking(id,db)
