from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)  # Specify length here
    password = Column(String(255), nullable=False)
    def __str__(self):
        return f"object : <id:{self.id} name:{self.username}>"

class Car(Base):
    __tablename__ = 'car'
    # ID, make, model, year, mileage, available now, minimum rent period,maximum rent period
    id = Column(Integer, primary_key=True)
    maker = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    mileage = Column(Integer, nullable=False)
    available_now = Column(Boolean, nullable=False,default=True)
    minimum_rent_period = Column(Integer, nullable=False)
    maximum_rent_period = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    booking_now = Column(Boolean, nullable=False, default=False, server_default='0')
    def __str__(self):
        return f"object : <id:{self.id} make:{self.maker} model:{self.model} year:{self.year} mileage:{self.mileage} available_now:{self.available_now} minimum_rent_period:{self.minimum_rent_period} maximum_rent_period:{self.maximum_rent_period}>"

# Create the mysql database engine and session
# engine = create_engine('mysql+pymysql://root:abcd=1234@localhost:3306/carrental')
#use memory databasase to save the trouble of additional database deployment
engine = create_engine('sqlite://',connect_args={'check_same_thread':False},poolclass=StaticPool)
SessionLocal = sessionmaker(bind=engine)


Base.metadata.create_all(engine)

def get_session():
    db = SessionLocal()
    return db
