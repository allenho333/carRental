from .models import User
from .db import get_db


# 根据用户名查询用户
def select_user_by_name(username: str):
    db = get_db()
    print("db", db)
    print("db.query(User)",db.query(User))
    print("db.query(User).filter(User.username == username)",db.query(User).filter(User.username == username))
    print("db.query(User).filter(User.username == username).all()",db.query(User).filter(User.username == username).all())
    return "test"
    # return get_db().query(User).filter(User.username == username).first()
