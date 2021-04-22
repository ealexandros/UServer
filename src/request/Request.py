from request.BodyParser import BodyParser
from helpers.RegexHelpers import uregex as re

class Request:
    '''
        Handles the request from the client. Parser the whole message and organises all the data.

        :request:   This is a String with the request from the client.
        :addr:      This is the ip address and the port from the client.
    '''
    def __init__(self, request, addr):
        self.__request = request
        self.__addr_ip = addr[0]
        self.__addr_port = addr[1]

        self.__request_method = None
        self.__http_path = None
        self.__http_path_list = None
        self.__http_version = None
        self.__headers = {}

        self.__content_type = None
        self.__params = {}
        self.url_params = {}
        self.__body = {}

        self.__parse_request()

    def __parse_request(self):
        self.__request_method = re.findall(r'[A-Z]+', self.__request[0])[0]
        self.__http_path = self.__request[0].replace(self.__request_method, '').strip().split(' ')[0]
        self.__http_path_list = list(map(lambda x: '/' + x, self.__http_path.split('/')[1:]))
        self.__http_version = re.findall(r'(HTTP[/][0-9.]*|HTTPS[/][0-9.]*)', self.__request[0])[0]

        for header in self.__request[1:]:
            if(header == '\r\n' or header == '\n'):
                break
            elif(':' in header):
                header_split = re.one_cut_split(r'[:]', header)
                self.__headers[header_split[0].strip()] =  header_split[1].strip()

        if('Content-Length' in self.__headers and int(self.__headers['Content-Length']) > 0):
            raw_body = self.__request[-1].strip()
            if('Content-Type' in self.__headers):
                self.__content_type = self.__headers['Content-Type']
            self.__body = BodyParser(raw_body)._get_parse_object(self.__content_type)

        if('?' in self.__request[0]):
            raw_params = re.findall(r"[?][A-Za-z0-9=_+!@#$&]+", self.__request[0])[0][1:]
            self.__params = BodyParser(raw_params)._get_parse_object('params')

    @property
    def method(self):
        return self.__request_method

    @property
    def path(self):
        return self.__http_path
    
    @property
    def path_list(self):
        return self.__http_path_list

    @property
    def http_version(self):
        return self.__http_version

    @property
    def addr(self):
        return self.__addr_ip

    @property
    def port(self):
        return self.__addr_port

    @property        
    def content_type(self):
        return self.__content_type

    def url_param(self, param):
        if(param in self.url_params):
            return self.url_params[param]
        return None

    def body(self, body_name):
        if(body_name in self.__body):
            return self.__body[body_name]
        return None

    def param(self, param_name):
        if(param_name in self.__params):
            return self.__params[param_name]
        return None

    def header(self, header_name):
        if(header_name in self.__headers):
            return self.__headers[header_name]
        return None