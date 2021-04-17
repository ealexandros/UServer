try:
    import json
except:
    import ujson

from response.HTTPResponseCodes import HTTP_STATUS_CODES

class Response:
    '''
        This class helps with the response of the server. It creates a basic template for the response.
        The server can add extra things like headers, different type of responses and also change the status code.

        :client:    This is a socket connection.
    '''
    def __init__(self, client):
        self.HTTP_VERSION = "HTTP/1.1"

        self.__client = client
        self.__status = 200
        self.server = 'ESP Micropython'
        self.connection = 'Keep-Alive'
        self.keep_alive = 'timeout=5'
        self.accept_ranges = 'bytes'
        self.accept = '*/*'

        self.__cors = None

    def send(self, data="", content_type='text/plain', headers={}):
        http_builder = "{} {} {}\r\n".format(self.HTTP_VERSION, self.__status, HTTP_STATUS_CODES[str(self.__status)])
        http_builder += "Server: {}\r\n".format(self.server)
        http_builder += "Connection: {}\r\n".format(self.connection)
        http_builder += "Keep-Alive: {}\r\n".format(self.keep_alive)
        http_builder += "Accept-Ranges: {}\r\n".format(self.accept_ranges)
        http_builder += "Accept: {}\r\n".format(self.accept)
        http_builder += "Content-Length: {}\r\n".format(len(data))

        if(self.__cors != None):
            http_builder += "Access-Control-Allow-Origin: {}\r\n".format(self.__cors)

        if(type(headers) == dict and len(headers) > 0):
            for key in headers:
                http_builder += "{}: {}\r\n".format(key, headers[key])

        if(data != ""):
            http_builder += "Content-Type: {}\r\n".format(content_type)
            http_builder += "\r\n{}".format(data)
        else:
            http_builder += "\r\n"

        byte_data = bytes(http_builder, 'utf-8')
        self.__client.send(byte_data)
        self.close()

    def send_plain(self, data, headers={}):
        self.send(data, 'text/plain', headers)

    def send_json(self, data, headers={}):
        data_to_json = json.dumps(data)
        self.send(data_to_json, 'application/json', headers)

    def send_html(self, data, headers={}):
        self.send(data, 'text/html', headers)

    def send_css(self, data, headers={}):
        self.send(data, 'text/css', headers)

    def send_javascript(self, data, headers={}):
        self.send(data, 'text/javascript', headers)

    def send_xml(self, data, headers={}):
        self.send(data, 'application/xml', headers)

    def send_content(self, path, data):
        extention = '.'.join(path.split('.')[1:])
        if(extention == 'html'):
            self.send_html(data)
        elif(extention == 'css'):
            self.send_css(data)
        elif(extention == 'js'):
            self.send_javascript(data)
        else:
            self.send_plain(data)

    def close(self):
        self.__client.close()

    def cors(self, value):
        self.__cors = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if(str(new_status) not in HTTP_STATUS_CODES):
            raise ValueError('Status code {} is incorrect.'.format(new_status))
        self.__status = new_status
