import unittest2
import requests

import json
import os
import sys
import re

sys.path.insert(1, os.path.abspath('./src/'))
from UServer import UServer

class RequestsTest(unittest2.TestCase):
    host = '127.0.0.1'
    port = 3000
    app = UServer(port, host=host)

    @classmethod
    def setUpClass(cls):
        cls.app.start()

    def test_documentation_points_1(self):
        @self.app.router.get("/one")
        def index(req, res):
            res.send("OK")

        json_response = requests.get(f"http://{self.host}:{self.port}/docs/json")
        html_response = requests.get(f"http://{self.host}:{self.port}/docs")

        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(html_response.status_code, 200)

        self.assertEqual(json_response.text, '[{"path": "/one", "method": "GET", "description": "", "status_codes": {}}]')
        self.assertEqual('<!DOCTYPE html>' in html_response.text, True)

    def test_documentation_points_3(self):
        @self.app.router.post("/two")
        def index(req, res):
            res.send("OK")

        @self.app.router.put("/three")
        def index(req, res):
            res.send("OK")

        json_response = requests.get(f"http://{self.host}:{self.port}/docs/json")
        html_response = requests.get(f"http://{self.host}:{self.port}/docs")

        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(html_response.status_code, 200)

        self.assertEqual(json_response.text, '[{"path": "/one", "method": "GET", "description": "", "status_codes": {}}, {"path": "/two", "method": "POST", "description": "", "status_codes": {}}, {"path": "/three", "method": "PUT", "description": "", "status_codes": {}}]')
        self.assertEqual('<!DOCTYPE html>' in html_response.text, True)

    def test_documentation_points_5(self):
        @self.app.router.patch("/four")
        def index(req, res):
            res.send("OK")

        @self.app.router.delete("/five")
        def index(req, res):
            res.send("OK")

        json_response = requests.get(f"http://{self.host}:{self.port}/docs/json")
        html_response = requests.get(f"http://{self.host}:{self.port}/docs")

        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(html_response.status_code, 200)

        self.assertEqual(json_response.text, '[{"path": "/one", "method": "GET", "description": "", "status_codes": {}}, {"path": "/two", "method": "POST", "description": "", "status_codes": {}}, {"path": "/three", "method": "PUT", "description": "", "status_codes": {}}, {"path": "/four", "method": "PATCH", "description": "", "status_codes": {}}, {"path": "/five", "method": "DELETE", "description": "", "status_codes": {}}]')
        self.assertEqual('<!DOCTYPE html>' in html_response.text, True)

    def test_documentation_points_multiple_entries(self):
        @self.app.router.patch("/four")
        def index(req, res):
            res.send("OK")

        @self.app.router.delete("/five")
        def index(req, res):
            res.send("OK")

        json_response = requests.get(f"http://{self.host}:{self.port}/docs/json")
        html_response = requests.get(f"http://{self.host}:{self.port}/docs")

        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(html_response.status_code, 200)

        self.assertEqual(json_response.text, '[{"path": "/one", "method": "GET", "description": "", "status_codes": {}}, {"path": "/two", "method": "POST", "description": "", "status_codes": {}}, {"path": "/three", "method": "PUT", "description": "", "status_codes": {}}, {"path": "/four", "method": "PATCH", "description": "", "status_codes": {}}, {"path": "/five", "method": "DELETE", "description": "", "status_codes": {}}]')
        self.assertEqual('<!DOCTYPE html>' in html_response.text, True)

    def test_documentation_points_param_info(self):
        @self.app.router.patch("/six", description="Patch request to six endpoint", return_codes={
            "200": "OK",
            "400": "Bad Request"
        })
        def index(req, res):
            res.send("OK")

        json_response = requests.get(f"http://{self.host}:{self.port}/docs/json")
        html_response = requests.get(f"http://{self.host}:{self.port}/docs")

        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(html_response.status_code, 200)

        self.assertEqual('description": "Patch request to six endpoint"' in json_response.text, True)
        self.assertEqual('<!DOCTYPE html>' in html_response.text, True)

    def test_documentation_points_string_info(self):
        @self.app.router.delete("/seven", docs='''
            description: Delete request to seven endpoint

            return_codes: {
                "200": "OK",
                "400": "Bad Request"
            }''')
        def index(req, res):
            res.send("OK")

        json_response = requests.get(f"http://{self.host}:{self.port}/docs/json")
        html_response = requests.get(f"http://{self.host}:{self.port}/docs")

        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(html_response.status_code, 200)

        self.assertEqual('description": "Delete request to seven endpoint"' in json_response.text, True)
        self.assertEqual('<!DOCTYPE html>' in html_response.text, True)

if (__name__ == "__main__"):
    unittest2.main()