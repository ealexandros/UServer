import unittest2
import requests

import json
import os
import sys
import re

sys.path.insert(1, os.path.abspath('./src/'))
from UServer import UServer
from UMiddlewares import *
from env import dotenv

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
                res.send("Cors not enabled")

        @cls.app.router.get("/middlewares/multiple/one", middlewares=[EnableCors, ParamValidation])
        def index(req, res):
            if(res.cors_state != None):
                res.send("OK")
            else:
                res.send("Cors not enabled")

        @cls.app.router.get("/middlewares/multiple/two", middlewares=[EnableCors, ParamValidation, BodyJson])
        def index(req, res):
            if(res.cors_state != None):
                res.send("OK")
            else:
                res.send("Cors not enabled")

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
        middleware_multiple_1_5 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/one', data='test', params={"status": "OK"})

        middleware_multiple_2_1 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/two')
        middleware_multiple_2_2 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/two', params={"status": "OK"})
        middleware_multiple_2_3 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/two', data='{"status": "OK"}', headers={'Content-Type': 'application/json'})
        middleware_multiple_2_4 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/two', data='{"status": "OK"}', params={"status": "OK"}, headers={'Content-Type': 'application/json'})
        middleware_multiple_2_5 = requests.get(f'http://{self.host}:{self.port}/middlewares/multiple/two', data='test', params={"status": "OK"})

        self.assertEqual(middleware_multiple_1_1.status_code, 200)
        self.assertEqual(middleware_multiple_1_2.status_code, 200)
        self.assertEqual(middleware_multiple_1_3.status_code, 200)
        self.assertEqual(middleware_multiple_1_4.status_code, 200)
        self.assertEqual(middleware_multiple_1_5.status_code, 200)

        self.assertEqual(middleware_multiple_2_1.status_code, 200)
        self.assertEqual(middleware_multiple_2_2.status_code, 200)
        self.assertEqual(middleware_multiple_2_3.status_code, 200)
        self.assertEqual(middleware_multiple_2_4.status_code, 200)
        self.assertEqual(middleware_multiple_2_5.status_code, 200)

        self.assertEqual(middleware_multiple_1_1.text, "OK")
        self.assertEqual(middleware_multiple_1_2.text, "OK")
        self.assertEqual(middleware_multiple_1_3.text, "OK")
        self.assertEqual(middleware_multiple_1_4.text, "OK")
        self.assertEqual(middleware_multiple_1_5.text, "OK")

        self.assertEqual(middleware_multiple_2_1.text, "OK")
        self.assertEqual(middleware_multiple_2_2.text, "OK")
        self.assertEqual(middleware_multiple_2_3.text, "OK")
        self.assertEqual(middleware_multiple_2_4.text, "OK")
        self.assertNotEqual(middleware_multiple_2_5.text, "OK")

    def test_static_file_folders(self):
        self.app.static('\\tests\\TestFiles\\static\\')

        static_file_1 = requests.get(f'http://{self.host}:{self.port}/tests/TestFiles/static/index.html')
        static_file_2 = requests.get(f'http://{self.host}:{self.port}/tests/TestFiles/static/css/style.css')

        self.assertEqual(static_file_1.status_code, 200)
        self.assertEqual(static_file_2.status_code, 200)

        self.assertEqual('<!DOCTYPE html>' in static_file_1.text, True)
        self.assertEqual('body {' in static_file_2.text, True)

    def test_dotenv_module(self):
        env = dotenv('tests\\TestFiles\\.env.test')
        env.scan()

        self.assertEqual(env['test_one'], "100")
        self.assertEqual(env['test_two'], "200")
        self.assertEqual(env['test_three'], "this is secret stuff")

if(__name__ == "__main__"):
    unittest2.main()