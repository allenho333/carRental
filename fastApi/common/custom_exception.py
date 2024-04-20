from common import error_enum


class CustomException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    # 方法重载 使其支持使用自定义枚举类进行初始化
    @classmethod
    def init(cls, e: error_enum.Error):
        return cls(e.code, e.msg)

    def __str__(self):
        return f"{self.code}: {self.message}"
