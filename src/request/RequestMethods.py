from helpers.RegexHelpers import uregex as re

class RequestMethods:
    '''
        This class handles all of the predifined server HTTP Methods. It simply adds to the
        UServer.__router_paths the paths the server wants to listen on.

        :userver:   A UServer object.
    '''
    def __init__(self, userver):
        self.__userver = userver
        self.valid_methods = ["GET", "POST", "PUT", "PATCH", "OPTIONS", "DELETE"]

    def __path_validation(self, path):
        if(path == '*'): return ['*']

        path_validation = re.findall(r'[/]([A-Za-z0-9_-]|[:]|[/]|[.]|[*])*', path)[0]
        if(path_validation != path):
            raise Exception('Invalid path name. Check your name again: ' + path)
        return re.findall(r'[/]([A-Za-z0-9_-]|[:]|[.]|[*])*', path)

    def handle_methods(self, path, callback, method, redirects=[], description='', return_codes={}, reverse_stack=False):
        path = self.__path_validation(path)
        redirects = list(map(lambda path: self.__path_validation(path), redirects))

        self.__userver.router_paths.append({
            'path': path,
            'callback': callback,
            'method': method,
            'redirects': redirects,
            'description': description,
            'return_codes': return_codes,
        })

        if(reverse_stack):
            last_route = self.__userver.router_paths.pop()
            self.__userver.router_paths.insert(0, last_route)

    def static_content(self, path, content):
        def callback(req, res):
            res.send_content(path, content)
        self.handle_methods(path, [callback], 'GET')

    def on(self, path, req_method, callback, middlewares=[], redirects=[], description='', return_codes={}, reverse_stack=False):
        if(req_method not in self.valid_methods):
            raise Exception('Invalid request type. You can only use:\n' + ", ".join(self.valid_methods) + '.')
        self.handle_methods(path, middlewares + [callback], req_method, redirects, description, return_codes, reverse_stack)

    def get(self, path, middlewares=[], redirects=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'GET', redirects, description, return_codes)
        return handler

    def post(self, path, middlewares=[], redirects=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'POST', redirects, description, return_codes)
        return handler

    def patch(self, path, middlewares=[], redirects=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'PATCH', redirects, description, return_codes)
        return handler

    def put(self, path, middlewares=[], redirects=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'PUT', redirects, description, return_codes)
        return handler

    def delete(self, path, middlewares=[], redirects=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'DELETE', redirects, description, return_codes)
        return handler

    def options(self, path, middlewares=[], redirects=[], description='', return_codes={}):
        def handler(callback):
            self.handle_methods(path, middlewares + [callback], 'OPTIONS', redirects, description, return_codes)
        return handler