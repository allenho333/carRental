from pydantic import BaseModel


class Car(BaseModel):
    maker: str
    model: str
    year: int
    mileage: int
    available_now: bool
    minimum_rent_period: int
    maximum_rent_period: int
    unit_price: int
    booking_now: bool
    def __str__(self):
        return f"object : <maker:{self.maker} model:{self.model} year:{self.year} mileage:{self.mileage} available_now:{self.available_now} minimum_rent_period:{self.minimum_rent_period} maximum_rent_period:{self.maximum_rent_period}>"