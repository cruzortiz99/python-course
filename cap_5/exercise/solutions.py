class CustomError(Exception):
    def __init__(self, message="Custom error raise"):
        super().__init__(message)


def raiseError():
    raise CustomError()


raiseError()
