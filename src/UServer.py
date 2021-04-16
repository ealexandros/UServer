import network

from request.Request import Request
from request.RequestMethods import RequestMethods
from request.Logger import Logger

from response.Response import Response
from response.BadRespond import BadRespond
from response.ErrorResponse import ErrorResponse

from helpers.RegexHelpers import uregex as re
from helpers.OSPath import upath

from docs.UDocs import UDocs

try:
    import usocket as socket
except:
    import socket

try:
    import threading
except:
    import _thread as threading

class UServer:
    def __init__(self, port, host='127.0.0.1'):
        self.__port = port
        self.__host = host

        self.__router_paths = []

        self.__error_respond = ErrorResponse()
        self.__request_methods = RequestMethods(self)
        self.logger = Logger()
        self.__docs = UDocs(self)

    @property
    def docs(self):
        return self.__docs

    @property
    def router_paths(self):
        return self.__router_paths

    @property
    def router(self):
        return self.__request_methods

    @property
    def error(self):
        return self.__error_respond

    @property
    def port(self):
        return self.__port

    @property
    def addr(self):
        if(self.__host == '0.0.0.0'):
            return network.WLAN(network.STA_IF).ifconfig()[0]
        return self.__host

    def __blocking_loop(self):
        try:
            while(True):
                pass
        except KeyboardInterrupt:
            exit(0)

    def start(self, logger=False, doc_path='/docs', show_doc=True, block=False, function=False):
        def handler(callback):
            callback()
            if(block):
                self.__blocking_loop()
                
        # if(True):
        if(network.WLAN(network.STA_IF).isconnected() or network.WLAN(network.AP_IF).active()):
            self.logger.active = logger
            if(show_doc):
                self.__docs.start(doc_path)

            self.__start_listening()
            threading.start_new_thread(self.__handle_server, ())
            # threading.Thread(target=self.__handle_server, daemon=True).start()

            if(function):
                return handler
            if(block):
                self.__blocking_loop()
        else:
            raise Exception('Wifi is not setup correctly.')

    def static(self, dir_name):
        base_path = '/' + dir_name.split(upath.get_correct_slash())[-1]
        if('.' in base_path):
            raise Exception('Invalid folder name: ' + base_path)

        try:
            for path, dirs, files in upath.walk(dir_name):
                path_validation = '.' + re.findall(r'[\\/]([A-Za-z0-9_-]|[\\/]|[.])*', path)[0]
                if(path_validation != path):
                    raise Exception('Invalid path name.')
                elif(any(list(filter(lambda x: '.' in x, dirs)))):
                    raise Exception('Invalid folder name. Folders must not contain . characters')

                middle_path = path.replace(dir_name, '/').replace(upath.get_correct_slash(), '/')[1:] + '/'
                for f in files:
                    with open(path + upath.get_correct_slash() + f, 'r') as fil:
                        self.router.static_content(base_path + middle_path + f, "".join(fil.readlines()))
        except Exception as e:
            print('Can\'t create static folder.')
            print(e)

    def __start_listening(self):
        addr = socket.getaddrinfo(self.__host, self.__port)[0][-1]
        self.conn = socket.socket()
        self.conn.bind(addr)
        self.conn.listen(1)

    def __router(self, __request, __response):
        url_params = {}
        for router in self.__router_paths:
            for __path in ([router['path']] + router['redirects']):
                if(router['method'] == __request.method and len(__path) == len(__request.path_list)):
                    for defined_path, req_path in list(zip(__path, __request.path_list)):
                        if(len(defined_path) > 1 and defined_path[1] == ':'):
                            url_params[defined_path[2:]] = req_path[1:]
                        elif(defined_path == '/*'):
                            continue
                        elif(defined_path != req_path):
                            break
                    else:
                        __request.url_params.update(url_params)
                        for callback in router['callback']:
                            __next = callback(__request, __response)
                            if(type(__next) == Exception):
                                self.__error_respond.call(__request, __response, str(__next))
                                return
                            elif(__next != True):
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
                http_request_body_split = re.one_cut_split("\r\n\r\n|\n\n", http_request_raw.strip())
                find_line_feed = lambda s: '\r\n' if('\r\n' in s) else '\n'
                http_request_list = http_request_body_split[0].split(find_line_feed(http_request_body_split[0])) \
                                        + [find_line_feed(http_request_body_split[0]), http_request_body_split[1]]

                if(http_request_raw != ''):
                    __request = Request(http_request_list, addr)
                    if(self.logger.active):
                        self.logger.action(__request)
                    __response = Response(client)
                    self.__router(__request, __response)
                else:
                    client.close()
            except:
                client.close()