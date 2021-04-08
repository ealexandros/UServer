# import network
import traceback

from request.Request import Request
from response.Response import Response
from response.BadRespond import BadRespond

from helpers.RegexHelpers import uregex as re

try:
    import usocket as socket
except:
    import socket

try:
    import threading
except:
    import _thread as threading

class UServer:
    def __init__(self, port, block=False, host='127.0.0.1'):
        self.__port = port
        self.__host = host
        self.__block = block

        self.__router_paths = []
        self.req_methods = ["GET", "POST", "PUT", "PATCH", "OPTIONS", "DELETE"]

    def start(self):
        # sta_if = network.WLAN(network.STA_IF)
        # if(sta_if.isconnected()):
        if(True):
            self.__start_listening()
            if(self.__block):
                self.__handle_server()
            else:
                # threading.start_new_thread(self.__handle_server, ())
                threading.Thread(target=self.__handle_server, daemon=True).start()
        else:
            raise Exception('No WIFI connection.')

    def handle_methods(self, path, callback, method):
        path_validation = re.findall(r'[/]([A-Za-z0-9_-]|[:]|[/])+', path)[0]
        if(path_validation != path):
            raise Exception('Invalid path name.')

        path = re.findall(r'([A-Za-z0-9_-]|[:])+', path)
        self.__router_paths.append([path, callback, method])

    def on(self, path, req_method, callback, middlewares=[]):
        if(req_method not in self.req_methods):
            raise Exception('Invalid request type. You can only use:\n' + ", ".join(self.req_methods) + '.')
        self.__router_paths.append([path, callback, middlewares + [req_method]])

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

    def __start_listening(self):
        addr = socket.getaddrinfo(self.__host, self.__port)[0][-1]
        self.conn = socket.socket()
        self.conn.bind(addr)
        self.conn.listen(1)

    def __router(self, __request, __response):
        url_params = {}
        for path, callbacks, method in self.__router_paths:
            if(method == __request.method and len(path) == len(__request.path_list)):
                for defined_path, req_path in list(zip(path, __request.path_list)):
                    if(defined_path[0] == ':'):
                        url_params[defined_path[1:]] = req_path
                    elif(defined_path != req_path):
                        break
                else:
                    __request.url_params.update(url_params)
                    for callback in callbacks:
                        __next = callback(__request, __response)
                        if(__next != True):
                            return
        BadRespond(__response, __request).send()

    def __handle_server(self):
        while(True):
            client, addr = self.conn.accept()
            client.setblocking(False)

            try:
                http_request_raw = ""
                while(True):
                    try:
                        http_request_raw += client.recv(1024).decode()
                    except:
                        break
                http_request_list = http_request_raw.strip().split(('\r\n' if('\r\n' in http_request_raw) else '\n'))

                if(http_request_raw != ''):
                    __request = Request(http_request_list, addr)
                    __response = Response(client)
                    self.__router(__request, __response)
            except:
                traceback.print_exc()
                client.close()

app = UServer(3000)

@app.get('/adfsd/:id')
def cool(req, res):
    res.send_json({ 'response': req.url_param('id') })

app.start()

while(True):
    pass