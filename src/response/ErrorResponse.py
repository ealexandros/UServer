class ErrorResponse:
    '''
        This class handles if an Exception isreturn in a function.
    '''
    def __init__(self):
        self.__error_response = self.__default_error_response

    def __default_error_response(self, req, res, error_messages=None):
        res.send_json({
            "errors": error_messages
        })

    def override(self):
        def handler(callback):
            self.__error_response = callback
        return handler

    def call(self, req, res, error_messages):
        self.__error_response(req, res, error_messages)
