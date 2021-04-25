import unittest2
import requests

import json
import os
import sys
import re

sys.path.insert(1, os.path.abspath('./src/'))
from request.Request import Request

class RequestsTest(unittest2.TestCase):
    def test_requests_variables_example_one(self):
        http_request = ['GET /person?test=sdfg HTTP/1.1', 'Accept: text/plain', 'Content-Type: application/json', 'Cache-Control: no-cache', 'Host: 127.0.0.1:3000', 'Accept-Encoding: gzip, deflate, br', 'Connection: keep-alive', 'Content-Length: 28', '\r\n', '{\r\n    "asdfsdf": "asfsd"\r\n}']
        __request = Request(http_request, ('127.0.0.1', 3000))
        
        self.assertEqual(__request._Request__request_method, 'GET')
        self.assertEqual(__request._Request__addr_ip, '127.0.0.1')
        self.assertEqual(__request._Request__addr_port, 3000)
        self.assertEqual(__request._Request__http_path, '/person')
        self.assertEqual(__request._Request__http_path_list, ['/person'])
        self.assertEqual(__request._Request__http_version, 'HTTP/1.1')
        self.assertEqual(__request._Request__headers, {
            'Accept': 'text/plain',
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'Host': '127.0.0.1:3000',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '28'
        })

    def test_requests_variables_example_two(self):
        http_request = ['GET /person?test=sdfg HTTP/1.1', 'Accept: text/plain', 'Cache-Control: no-cache', 'Host: 127.0.0.1:3000', 'Accept-Encoding: gzip, deflate, br', 'Connection: keep-alive', 'Content-Type: application/x-www-form-urlencoded', 'Content-Length: 9', '\r\n', 'test=sdfg']
        __request = Request(http_request, ('127.0.0.1', 3000))

        self.assertEqual(__request._Request__request_method, 'GET')
        self.assertEqual(__request._Request__addr_ip, '127.0.0.1')
        self.assertEqual(__request._Request__addr_port, 3000)
        self.assertEqual(__request._Request__http_path, '/person')
        self.assertEqual(__request._Request__http_path_list, ['/person'])
        self.assertEqual(__request._Request__http_version, 'HTTP/1.1')
        self.assertEqual(__request._Request__headers, {
            'Accept': 'text/plain',
            'Cache-Control': 'no-cache',
            'Host': '127.0.0.1:3000',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '9'
        })

if(__name__ == '__main__'):
    unittest2.main()