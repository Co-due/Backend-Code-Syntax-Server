from app.route.services.exception.enum.error_enum import ErrorEnum
from starlette import status


class BaseCustomException(Exception):
    def __init__(self, status_code: status, error_enum: ErrorEnum, result: dict = None):
        self.status = status_code
        self.error_enum = error_enum
        self.result = {} if result is None else result
