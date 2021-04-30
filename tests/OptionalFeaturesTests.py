import unittest2
import requests

import json
import os
import sys
import re

sys.path.insert(1, os.path.abspath('./src/'))
from UServer import UServer
from UMiddlewares import *

class RequestsTest(unittest2.TestCase):
    host = '127.0.0.1'
    port = 3000
    app = UServer(port=port, host=host)

    @classmethod
    def setUpClass(cls):
        @cls.app.router.get("/body/json", middlewares=[BodyJson])
        def index(req, res):
            res.send("OK")

        @cls.app.router.get("/params", middlewares=[ParamValidation])
        def index(req, res):
            res.send("OK")
            
        @cls.app.router.get("/logs", middlewares=[RequestLog])
        def index(req, res):
            res.send("OK")
            
        @cls.app.router.get("/cors", middlewares=[EnableCors])
        def index(req, res):
            if(res.cors_state != None):
                res.send("OK")
            else:
                res.send("BAD")

        @cls.app.router.get("/middlewares/multiple/one", middlewares=[EnableCors, ParamValidation])
        def index(req, res):
            res.send("OK")

        @cls.app.router.get("/middlewares/multiple/two", middlewares=[EnableCors, ParamValidation, BodyJson])
        def index(req, res):
            res.send("OK")

        cls.app.start()

    def test_all_built_in_middlewares(self):
        middleware_json_test_1 = requests.get(f'http://{self.host}:{self.port}/body/json', data='{"status": "OK"}', headers={'Content-Type': 'application/json'})
        middleware_json_test_2 = requests.get(f'http://{self.host}:{self.port}/body/json', headers={'Content-Type': 'application/json'})
        middleware_json_test_3 = requests.get(f'http://{self.host}:{self.port}/body/json', data='{"status": "OK"}')
        middleware_json_test_4 = requests.get(f'http://{self.host}:{self.port}/body/json', data='testing')

        middleware_param_test_1 = requests.get(f'http://{self.host}:{self.port}/params', params={"status": "OK"})
        middleware_param_test_2 = requests.get(f'http://{self.host}:{self.port}/params', params={"status": "OK", "status_2": True})
        middleware_param_test_3 = requests.get(f'http://{self.host}:{self.port}/params')

        middleware_logs = requests.get(f'http://{self.host}:{self.port}/logs')
        middleware_cors = requests.get(f'http://{self.host}:{self.port}/cors')

        self.assertEqual(middleware_json_test_1.status_code, 200)
        self.assertEqual(middleware_json_test_2.status_code, 200)
        self.assertEqual(middleware_json_test_3.status_code, 200)
        self.assertEqual(middleware_json_test_4.status_code, 200)

        self.assertEqual(middleware_param_test_1.status_code, 200)
        self.assertEqual(middleware_param_test_2.status_code, 200)
        self.assertEqual(middleware_param_test_3.status_code, 200)

        self.assertEqual(middleware_logs.status_code, 200)
        self.assertEqual(middleware_cors.status_code, 200)

        self.assertEqual(middleware_json_test_1.text, "OK")
        self.assertEqual(middleware_json_test_2.text, "OK")
        self.assertEqual(middleware_json_test_3.text, '{"errors": "Invalid body content. BodyParser error."}')
        self.assertEqual(middleware_json_test_4.text, '{"errors": "Invalid body content. BodyParser error."}')

        self.assertEqual(middleware_param_test_1.text, "OK")
        self.assertEqual(middleware_param_test_2.text, "OK")
        self.assertEqual(middleware_param_test_3.text, "OK")
        
        self.assertEqual(middleware_logs.text, "OK")
        self.assertEqual(middleware_cors.text, "OK")

    def test_multiple_middlewares(self):
        middleware_multiple_1_1 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/one')
        middleware_multiple_1_2 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/one', params={"status": "OK"})
        middleware_multiple_1_3 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/one', data='{"status": "OK"}')
        middleware_multiple_1_4 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/one', data='{"status": "OK"}', params={"status": "OK"})
        middleware_multiple_1_4 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/one', data='test', params={"status": "OK"})

        middleware_multiple_2 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/two', params={"status": "OK"})

        self.assertEqual(middleware_multiple_1.text, "OK")
        self.assertEqual(middleware_multiple_2.text, "OK")


if(__name__ == "__main__"):
    unittest2.main()