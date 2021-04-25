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
    app = UServer(port=port, host=host)

    @classmethod
    def setUpClass(cls):
        @cls.app.router.get('/get')
        def get(req, res):
            res.send("{}".format(req.param('param1')))

        @cls.app.router.post('/post')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.put('/put')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.patch('/patch')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.delete('/delete')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.head('/head')
        def get(req, res):
            res.send("{}".format(req.param('param1')))

        cls.app.start()

    def test_url_parameter_one(self):
        param = 'OK'
        get = requests.get(f'http://{self.host}:{self.port}/get', params={ 'param1': param })
        post = requests.post(f'http://{self.host}:{self.port}/post', params={ 'param1': param })
        patch = requests.patch(f'http://{self.host}:{self.port}/patch', params={ 'param1': param })
        put = requests.put(f'http://{self.host}:{self.port}/put', params={ 'param1': param })
        delete = requests.delete(f'http://{self.host}:{self.port}/delete', params={ 'param1': param })
        head = requests.head(f'http://{self.host}:{self.port}/head', params={ 'param1': param })

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, 'OK')
        self.assertEqual(post.text, 'OK')
        self.assertEqual(patch.text, 'OK')
        self.assertEqual(put.text, 'OK')
        self.assertEqual(delete.text, 'OK')
        self.assertEqual(head.text, '')

    def test_url_parameter_none(self):
        param = 'OK'
        get = requests.get(f'http://{self.host}:{self.port}/get')
        post = requests.post(f'http://{self.host}:{self.port}/post')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch')
        put = requests.put(f'http://{self.host}:{self.port}/put')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete')
        head = requests.head(f'http://{self.host}:{self.port}/head')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, 'None')
        self.assertEqual(post.text, 'None')
        self.assertEqual(patch.text, 'None')
        self.assertEqual(put.text, 'None')
        self.assertEqual(delete.text, 'None')
        self.assertEqual(head.text, '')

if(__name__ == "__main__"):
    unittest2.main()