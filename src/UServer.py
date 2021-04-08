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

    def on(self, path, req_method, callback):
        if(req_method not in self.req_methods):
            raise Exception('Invalid request type. You can only use:\n' + ", ".join(self.req_methods) + '.')
        self.__router_paths.append([path, callback, req_method])

    def get(self, path, callback):
        path = re.findall(r'([A-Za-z0-9_-]|[:])+', path)
        self.__router_paths.append([path, callback, 'GET'])

    def post(self, path, callback):
        self.__router_paths.append([path, callback, 'POST'])

    def patch(self, path, callback):
        self.__router_paths.append([path, callback, 'PATCH'])

    def put(self, path, callback):
        self.__router_paths.append([path, callback, 'PUT'])

    def delete(self, path, callback):
        self.__router_paths.append([path, callback, 'DELETE'])

    def options(self, path, callback):
        self.__router_paths.append([path, callback, 'OPTIONS'])

    @staticmethod
    def route(callback):
        def handler(__request, __response):
            return callback(__request, __response)
        return handler

    def __start_listening(self):
        addr = socket.getaddrinfo(self.__host, self.__port)[0][-1]
        self.conn = socket.socket()
        self.conn.bind(addr)
        self.conn.listen(1)

    def __router(self, __request, __response):
        url_params = {}
        for path, callback, method in self.__router_paths:
            if(method == __request.method and len(path) == len(__request.path_list)):
                for defined_path, req_path in list(zip(path, __request.path_list)):
                    if(defined_path[0] == ':'):
                        url_params[defined_path[1:]] = req_path
                    elif(defined_path != req_path):
                        break
                else:
                    __request.url_params.update(url_params)
                    callback(__request, __response)
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

@app.route
def cool(req, res):
    res.send_json({ 'response': True })

app.get('/cpp/:aghsg/:afsfa', cool)
app.start()

while(True):
    pass