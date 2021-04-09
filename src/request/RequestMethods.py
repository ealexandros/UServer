from helpers.RegexHelpers import uregex as re

class RequestMethods:
    def __init__(self, userver):
        self.userver = userver
        self.valid_methods = ["GET", "POST", "PUT", "PATCH", "OPTIONS", "DELETE"]

    def handle_methods(self, path, callback, method):
        path_validation = re.findall(r'[/]([A-Za-z0-9_-]|[:]|[/])+', path)[0]
        if(path_validation != path):
            raise Exception('Invalid path name.')

        path = re.findall(r'([A-Za-z0-9_-]|[:])+', path)
        self.userver.router_paths.append([path, callback, method])

    def on(self, path, req_method, callback, middlewares=[]):
        if(req_method not in self.valid_methods):
            raise Exception('Invalid request type. You can only use:\n' + ", ".join(self.valid_methods) + '.')
        self.handle_methods(path, middlewares + [callback], req_method)

    def get(self, path, middlewares=[]):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'GET')
        return handler

    def post(self, path, middlewares=[]):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'POST')
        return handler

    def patch(self, path, middlewares=[]):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'PATCH')
        return handler

    def put(self, path, middlewares=[]):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'PUT')
        return handler

    def delete(self, path, middlewares=[]):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'DELETE')
        return handler

    def options(self, path, middlewares=[]):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'OPTIONS')
        return handler