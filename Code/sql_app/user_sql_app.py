from config.database import User
from .db import get_db


# 根据用户名查询用户
def select_user_by_name(username: str):
    db = get_db()
    return get_db().query(User).filter(User.username == username).first()
