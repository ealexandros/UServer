from helpers.RegexHelpers import uregex as re

class RequestMethods:
    def __init__(self, userver):
        self.__userver = userver
        self.valid_methods = ["GET", "POST", "PUT", "PATCH", "OPTIONS", "DELETE"]

    def handle_methods(self, path, callback, method, docs):
        path_validation = re.findall(r'[/]([A-Za-z0-9_-]|[:]|[/]|[.])*', path)[0]
        if(path_validation != path):
            raise Exception('Invalid path name.')

        path = re.findall(r'[/]([A-Za-z0-9_-]|[:]|[.])*', path)
        self.__userver.router_paths.append([path, callback, method, docs])

    def static_content(self, path, content):
        def callback(req, res):
            res.send_content(path, content)
        self.handle_methods(path, [callback], 'GET', [])

    def on(self, path, req_method, callback, middlewares=[], description='', return_codes={}):
        if(req_method not in self.valid_methods):
            raise Exception('Invalid request type. You can only use:\n' + ", ".join(self.valid_methods) + '.')
        self.handle_methods(path, middlewares + [callback], req_method, [description, return_codes])

    def get(self, path, middlewares=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'GET', [description, return_codes])
        return handler

    def post(self, path, middlewares=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'POST', [description, return_codes])
        return handler

    def patch(self, path, middlewares=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'PATCH', [description, return_codes])
        return handler

    def put(self, path, middlewares=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'PUT', [description, return_codes])
        return handler

    def delete(self, path, middlewares=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'DELETE', [description, return_codes])
        return handler

    def options(self, path, middlewares=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'OPTIONS', [description, return_codes])
        return handler