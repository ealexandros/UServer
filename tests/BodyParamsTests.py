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
        @cls.app.router.get('/get/param/one')
        def get(req, res):
            res.send("{}".format(req.param('param1')))

        @cls.app.router.post('/post/param/one')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.put('/put/param/one')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.patch('/patch/param/one')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.delete('/delete/param/one')
        def get(req, res):
            res.send("{}".format(req.param('param1')))
            
        @cls.app.router.head('/head/param/one')
        def get(req, res):
            res.send("{}".format(req.param('param1')))

        @cls.app.router.get('/get/param/two')
        def get(req, res):
            res.send("{} {}".format(req.param('param1'), req.param('param2')))

        @cls.app.router.post('/post/param/two')
        def get(req, res):
            res.send("{} {}".format(req.param('param1'), req.param('param2')))
            
        @cls.app.router.put('/put/param/two')
        def get(req, res):
            res.send("{} {}".format(req.param('param1'), req.param('param2')))
            
        @cls.app.router.patch('/patch/param/two')
        def get(req, res):
            res.send("{} {}".format(req.param('param1'), req.param('param2')))
            
        @cls.app.router.delete('/delete/param/two')
        def get(req, res):
            res.send("{} {}".format(req.param('param1'), req.param('param2')))
            
        @cls.app.router.head('/head/param/two')
        def get(req, res):
            res.send("{} {}".format(req.param('param1'), req.param('param2')))

        @cls.app.router.get('/get/body/plain')
        def get(req, res):
            res.send("{}".format(req.body('__raw__')))

        @cls.app.router.post('/post/body/plain')
        def get(req, res):
            res.send("{}".format(req.body('__raw__')))
            
        @cls.app.router.put('/put/body/plain')
        def get(req, res):
            res.send("{}".format(req.body('__raw__')))
            
        @cls.app.router.patch('/patch/body/plain')
        def get(req, res):
            res.send("{}".format(req.body('__raw__')))
            
        @cls.app.router.delete('/delete/body/plain')
        def get(req, res):
            res.send("{}".format(req.body('__raw__')))
            
        @cls.app.router.head('/head/body/plain')
        def get(req, res):
            res.send("{}".format(req.body('__raw__')))

        @cls.app.router.get('/get/body/json')
        def get(req, res):
            res.send("{}".format(req.body('status')))

        @cls.app.router.post('/post/body/json')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.put('/put/body/json')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.patch('/patch/body/json')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.delete('/delete/body/json')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.head('/head/body/json')
        def get(req, res):
            res.send("{}".format(req.body('status')))



        @cls.app.router.get('/get/body/form')
        def get(req, res):
            res.send("{}".format(req.body('status')))

        @cls.app.router.post('/post/body/form')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.put('/put/body/form')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.patch('/patch/body/form')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.delete('/delete/body/form')
        def get(req, res):
            res.send("{}".format(req.body('status')))
            
        @cls.app.router.head('/head/body/form')
        def get(req, res):
            res.send("{}".format(req.body('status')))

        cls.app.start()

    def test_url_parameter_one(self):
        param = 'OK'
        get = requests.get(f'http://{self.host}:{self.port}/get/param/one', params={ 'param1': param })
        post = requests.post(f'http://{self.host}:{self.port}/post/param/one', params={ 'param1': param })
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/param/one', params={ 'param1': param })
        put = requests.put(f'http://{self.host}:{self.port}/put/param/one', params={ 'param1': param })
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/param/one', params={ 'param1': param })
        head = requests.head(f'http://{self.host}:{self.port}/head/param/one', params={ 'param1': param })

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, param)
        self.assertEqual(post.text, param)
        self.assertEqual(patch.text, param)
        self.assertEqual(put.text, param)
        self.assertEqual(delete.text, param)
        self.assertEqual(head.text, '')

    def test_url_parameter_two(self):
        param1, param2 = 'OK_1', 'OK_2'
        get = requests.get(f'http://{self.host}:{self.port}/get/param/two', params={ 'param1': param1, 'param2': param2 })
        post = requests.post(f'http://{self.host}:{self.port}/post/param/two', params={ 'param1': param1, 'param2': param2 })
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/param/two', params={ 'param1': param1, 'param2': param2 })
        put = requests.put(f'http://{self.host}:{self.port}/put/param/two', params={ 'param1': param1, 'param2': param2 })
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/param/two', params={ 'param1': param1, 'param2': param2 })
        head = requests.head(f'http://{self.host}:{self.port}/head/param/two', params={ 'param1': param1, 'param2': param2 })

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, f'{param1} {param2}')
        self.assertEqual(post.text, f'{param1} {param2}')
        self.assertEqual(patch.text, f'{param1} {param2}')
        self.assertEqual(put.text, f'{param1} {param2}')
        self.assertEqual(delete.text, f'{param1} {param2}')
        self.assertEqual(head.text, '')

    def test_url_parameter_none(self):
        param = 'OK'
        get = requests.get(f'http://{self.host}:{self.port}/get/param/one')
        post = requests.post(f'http://{self.host}:{self.port}/post/param/one')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/param/one')
        put = requests.put(f'http://{self.host}:{self.port}/put/param/one')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/param/one')
        head = requests.head(f'http://{self.host}:{self.port}/head/param/one')

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

    def test_body_type_plain(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/plain', data='OK')
        post = requests.post(f'http://{self.host}:{self.port}/post/body/plain', data='OK')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/plain', data='OK')
        put = requests.put(f'http://{self.host}:{self.port}/put/body/plain', data='OK')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/plain', data='OK')
        head = requests.head(f'http://{self.host}:{self.port}/head/body/plain', data='OK')

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

    def test_body_type_plain_none(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/plain')
        post = requests.post(f'http://{self.host}:{self.port}/post/body/plain')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/plain')
        put = requests.put(f'http://{self.host}:{self.port}/put/body/plain')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/plain')
        head = requests.head(f'http://{self.host}:{self.port}/head/body/plain')

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

    def test_body_type_json_no_header(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/json', data='{"status": "OK"}')
        post = requests.post(f'http://{self.host}:{self.port}/post/body/json', data='{"status": "OK"}')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/json', data='{"status": "OK"}')
        put = requests.put(f'http://{self.host}:{self.port}/put/body/json', data='{"status": "OK"}')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/json', data='{"status": "OK"}')
        head = requests.head(f'http://{self.host}:{self.port}/head/body/json', data='{"status": "OK"}')

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

    def test_body_type_json_with_header(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/json', data='{"status": "OK"}', headers={ 'Content-Type': 'application/json'})
        post = requests.post(f'http://{self.host}:{self.port}/post/body/json', data='{"status": "OK"}', headers={ 'Content-Type': 'application/json'})
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/json', data='{"status": "OK"}', headers={ 'Content-Type': 'application/json'})
        put = requests.put(f'http://{self.host}:{self.port}/put/body/json', data='{"status": "OK"}', headers={ 'Content-Type': 'application/json'})
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/json', data='{"status": "OK"}', headers={ 'Content-Type': 'application/json'})
        head = requests.head(f'http://{self.host}:{self.port}/head/body/json', data='{"status": "OK"}', headers={ 'Content-Type': 'application/json'})

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

    def test_body_type_form_with_header(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/form', data='status=OK', headers={ 'Content-Type': 'application/x-www-form-urlencoded'})
        post = requests.post(f'http://{self.host}:{self.port}/post/body/form', data='status=OK', headers={ 'Content-Type': 'application/x-www-form-urlencoded'})
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/form', data='status=OK', headers={ 'Content-Type': 'application/x-www-form-urlencoded'})
        put = requests.put(f'http://{self.host}:{self.port}/put/body/form', data='status=OK', headers={ 'Content-Type': 'application/x-www-form-urlencoded'})
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/form', data='status=OK', headers={ 'Content-Type': 'application/x-www-form-urlencoded'})
        head = requests.head(f'http://{self.host}:{self.port}/head/body/form', data='status=OK', headers={ 'Content-Type': 'application/x-www-form-urlencoded'})

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

    def test_body_type_form_no_header(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/form', data='status=OK')
        post = requests.post(f'http://{self.host}:{self.port}/post/body/form', data='status=OK')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/form', data='status=OK')
        put = requests.put(f'http://{self.host}:{self.port}/put/body/form', data='status=OK')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/form', data='status=OK')
        head = requests.head(f'http://{self.host}:{self.port}/head/body/form', data='status=OK')

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