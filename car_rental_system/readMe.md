# Car Rental

!MIT License

## licencing

Copyright (c) [2024] [Car Rental]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Introduction

This is a car rental system which allow users to check the cars and book cars, admins to add, delete, and updat cars ,  handle the bookings. it also allow users to signup and login.

### Installation

1. Clone the Repository

```bash
git clone https://github.com/allenho333/carRental.git
cd car_rental_system
```

2. Install Required Packages

```bash
pip install -r requirements.txt
```

1. Run the Application

```bash
python main.py
```

to start  the project

there are 2 default roles:
admin:
username: admin
password: admin

role:
username: role
passsword: role

there are 3 cars in memeory database in default

## Features

- signup
- login
- add, delete and update cars
- bookings
- accept booking
- reject booking
  
## File Structure

- main.py - The entry point of the application. It handles initialization and starting the command-line interface.
- /models
  - car.py - Defines the Car model.
  - user.py - Defines the User model.
- /sql_app
  - models.py - Configures the database connection and session.
  - db.py - initialize the database
  - user_sql_app - methods to handle the databaser
- /service
  - car.py - Manages car-related operations.
  - user.py - Manages user operations.
- requirements.txt - Lists all Python packages that need to be installed.

## Bugs or Issues

1. can only signup at the beginning
2. only support command line and do not provde a UI interface.

## Credits

  ** Contributors
     Guanghong He [https://github.com/allenho333]

  ** Third-Party Libraries
      [sqlAlchemy](https://www.sqlalchemy.org/) this library is a python toolkit to handle the database such as sqlite which is used in this project
