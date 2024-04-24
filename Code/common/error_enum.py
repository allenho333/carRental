from enum import Enum


# 错误枚举类
# 1xx 用户操作相关错误
# ...
class Error(Enum):
    USER_CREATE_PARAMETER_ERROR = ('100', '用户创建失败,参数错误')

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
