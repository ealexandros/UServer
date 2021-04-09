class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ErrorResponse(metaclass=SingletonMeta):
    __error_response = None
    
    def __init__(self):
        ErrorResponse.__error_response = self.__default_error_response

    def __default_error_response(self, req, res, error_messages=None):
        res.send_json({
            "errors": error_messages
        })

    @staticmethod
    def override():
        def handler(callback):
            ErrorResponse.__error_response = callback
        return handler

    def call(self, req, res, error_messages):
        ErrorResponse.__error_response(req, res, error_messages)
