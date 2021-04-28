from helpers.RegexHelpers import uregex as re

try:
    import json
except:
    import ujson as json

class RequestMethods:
    '''
        This class handles all of the predifined server HTTP Methods. It simply adds to the
        UServer.__router_paths the paths the server wants to listen on.

        :userver:   A UServer object.
    '''
    def __init__(self, userver):
        self.__userver = userver
        self.valid_methods = ["GET", "POST", "PUT", "PATCH", "HEAD", "DELETE"]

    def __path_validation(self, path):
        if(path == '*'): return ['*']

        path_validation = re.findall(r'[/]([A-Za-z0-9_-]|[:]|[/]|[.]|[*])*', path)[0]
        if(path_validation != path):
            raise Exception('Invalid path name. Check your name again: ' + path)
        return re.findall(r'[/]([A-Za-z0-9_-]|[:]|[.]|[*])*', path)
    
    def __check_method_doc(self, description, return_codes, doc_str):
        if(doc_str != None):
            doc_no_new_lines = "".join(list(map(lambda line: line.strip(), doc_str.split('\n'))))
            try:
                if('description: ' in doc_no_new_lines and 'return_codes: ' in doc_no_new_lines):
                    description, return_codes = doc_no_new_lines.split('return_codes: ')
                    description = description.replace('description: ', '').strip()
                    if(description[0] == '{' and return_codes[0] != '{'):
                        description, return_codes = return_codes, description
                    return_codes = json.loads(return_codes.replace('return_codes: ', '').strip())
                elif('description: ' in doc_no_new_lines):
                    description = doc_no_new_lines.split('description: ')[1]
                elif('return_codes: ' in doc_no_new_lines):
                    return_codes = doc_no_new_lines.split('return_codes: ')[1]
                    return_codes = json.loads(return_codes)
            except:
                print("ValueError: Your method documentation is not correct: " + str(doc_str))
        return description, return_codes

    def handle_methods(self, path, callback, method, redirects=[], description='', return_codes={}, reverse_stack=False):
        path = self.__path_validation(path)
        redirects = list(map(lambda path: self.__path_validation(path), redirects))

        duplicate_routes = list(filter(lambda route: route['path'] == path and route['method'] == method, self.__userver.router_paths))
        if(not duplicate_routes):
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
        else:
            print("LogicError: The path to the {} with the method {} already exists".format("".join(path), method))


    def static_content(self, path, content):
        def callback(req, res):
            res.send_file_content(path, content)
        self.handle_methods(path, [callback], 'GET')

    def restful(self, path, class_args=(), middlewares=[], redirects=[], description="", docs="", return_codes={}):
        def handler(RestObject):
            __instance = RestObject()
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            for method in dir(__instance):
                if(method.upper() in self.valid_methods):
                    callback = getattr(__instance, method)
                    self.handle_methods(path, middlewares + [callback], method.upper(), redirects, n_description, n_return_codes)
        return handler

    def on(self, path, req_method, callback, middlewares=[], redirects=[], description='', return_codes={}, docs="", reverse_stack=False):
        if(req_method not in self.valid_methods):
            raise Exception('Invalid request type. You can only use:\n' + ", ".join(self.valid_methods) + '.')
        n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
        self.handle_methods(path, middlewares + [callback], req_method, redirects, n_description, n_return_codes, reverse_stack)

    def get(self, path, middlewares=[], redirects=[], description='', return_codes={}, docs=""):
        def handler(callback):
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            self.handle_methods(path, middlewares + [callback], 'GET', redirects, n_description, n_return_codes)
        return handler

    def post(self, path, middlewares=[], redirects=[], description='', return_codes={}, docs=""):
        def handler(callback):
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            self.handle_methods(path, middlewares + [callback], 'POST', redirects, n_description, n_return_codes)
        return handler

    def patch(self, path, middlewares=[], redirects=[], description='', return_codes={}, docs=""):
        def handler(callback):
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            self.handle_methods(path, middlewares + [callback], 'PATCH', redirects, n_description, n_return_codes)
        return handler

    def put(self, path, middlewares=[], redirects=[], description='', return_codes={}, docs=""):
        def handler(callback):
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            self.handle_methods(path, middlewares + [callback], 'PUT', redirects, n_description, n_return_codes)
        return handler

    def delete(self, path, middlewares=[], redirects=[], description='', return_codes={}, docs=""):
        def handler(callback):
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            self.handle_methods(path, middlewares + [callback], 'DELETE', redirects, n_description, n_return_codes)
        return handler

    def head(self, path, middlewares=[], redirects=[], description='', return_codes={}, docs=""):
        def handler(callback):
            n_description, n_return_codes = self.__check_method_doc(description, return_codes, docs)
            self.handle_methods(path, middlewares + [callback], 'HEAD', redirects, n_description, n_return_codes)
        return handler