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
        @cls.app.router.get('/get/body/plain')
        def get(req, res):
            res.send('OK')

        @cls.app.router.post('/post/body/plain')
        def get(req, res):
            res.send('OK')
            
        @cls.app.router.put('/put/body/plain')
        def get(req, res):
            res.send('OK')
            
        @cls.app.router.patch('/patch/body/plain')
        def get(req, res):
            res.send('OK')
            
        @cls.app.router.delete('/delete/body/plain')
        def get(req, res):
            res.send('OK')
            
        @cls.app.router.head('/head/body/plain')
        def get(req, res):
            res.send('OK')

        @cls.app.router.get('/get/body/json')
        def get(req, res):
            res.send_json({ 'status': 'OK' })

        @cls.app.router.post('/post/body/json')
        def get(req, res):
            res.send_json({ 'status': 'OK' })
            
        @cls.app.router.put('/put/body/json')
        def get(req, res):
            res.send_json({ 'status': 'OK' })
            
        @cls.app.router.patch('/patch/body/json')
        def get(req, res):
            res.send_json({ 'status': 'OK' })
            
        @cls.app.router.delete('/delete/body/json')
        def get(req, res):
            res.send_json({ 'status': 'OK' })
            
        @cls.app.router.head('/head/body/json')
        def get(req, res):
            res.send_json({ 'status': 'OK' })

        @cls.app.router.get('/get/body/json/extra/one')
        def get(req, res):
            res.send_json({ "status": 100 })

        @cls.app.router.get('/get/body/json/extra/two')
        def get(req, res):
            res.send_json('OK')
            
        @cls.app.router.get('/get/body/json/extra/three')
        def get(req, res):
            res.send_json('this is a test')

        @cls.app.router.get('/get/body/plain/extra/one')
        def get(req, res):
            res.send_plain({ "status": "OK" })

        @cls.app.router.get('/get/body/plain/extra/two')
        def get(req, res):
            res.send_plain({ "status": 1000 })

        @cls.app.router.get('/get/body/plain/extra/three')
        def get(req, res):
            res.send_plain({ "status": True })

        @cls.app.router.get('/get/html')
        def get(req, res):
            res.send_html('''<html></html>''')

        @cls.app.router.post('/post/html')
        def get(req, res):
            res.send_html('''<html></html>''')
            
        @cls.app.router.put('/put/html')
        def get(req, res):
            res.send_html('''<html></html>''')
            
        @cls.app.router.patch('/patch/html')
        def get(req, res):
            res.send_html('''<html></html>''')
            
        @cls.app.router.delete('/delete/html')
        def get(req, res):
            res.send_html('''<html></html>''')
           
        @cls.app.router.head('/head/html')
        def get(req, res):
            res.send_html('''<html></html>''')

        @cls.app.router.get('/get/css')
        def get(req, res):
            res.send_css('''body {color: #fff}''')

        @cls.app.router.post('/post/css')
        def get(req, res):
            res.send_css('''body {color: #fff}''')
            
        @cls.app.router.put('/put/css')
        def get(req, res):
            res.send_css('''body {color: #fff}''')
            
        @cls.app.router.patch('/patch/css')
        def get(req, res):
            res.send_css('''body {color: #fff}''')
            
        @cls.app.router.delete('/delete/css')
        def get(req, res):
            res.send_css('''body {color: #fff}''')
           
        @cls.app.router.head('/head/css')
        def get(req, res):
            res.send_css('''body {color: #fff}''')

        @cls.app.router.get('/get/javascript')
        def get(req, res):
            res.send_javascript('''const x = 10''')

        @cls.app.router.post('/post/javascript')
        def get(req, res):
            res.send_javascript('''const x = 10''')
            
        @cls.app.router.put('/put/javascript')
        def get(req, res):
            res.send_javascript('''const x = 10''')
            
        @cls.app.router.patch('/patch/javascript')
        def get(req, res):
            res.send_javascript('''const x = 10''')
            
        @cls.app.router.delete('/delete/javascript')
        def get(req, res):
            res.send_javascript('''const x = 10''')
           
        @cls.app.router.head('/head/javascript')
        def get(req, res):
            res.send_javascript('''const x = 10''')

        cls.app.start()

    def test_body_plain_response(self):
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

        self.assertEqual(get.text, 'OK')
        self.assertEqual(post.text, 'OK')
        self.assertEqual(patch.text, 'OK')
        self.assertEqual(put.text, 'OK')
        self.assertEqual(delete.text, 'OK')
        self.assertEqual(head.text, '')

    def test_body_json_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/body/json')
        post = requests.post(f'http://{self.host}:{self.port}/post/body/json')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/body/json')
        put = requests.put(f'http://{self.host}:{self.port}/put/body/json')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/body/json')
        head = requests.head(f'http://{self.host}:{self.port}/head/body/json')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertRaises(TypeError, json.loads(get.text))
        self.assertRaises(TypeError, json.loads(post.text))
        self.assertRaises(TypeError, json.loads(patch.text))
        self.assertRaises(TypeError, json.loads(put.text))
        self.assertRaises(TypeError, json.loads(delete.text))

        self.assertEqual(json.loads(get.text)['status'], 'OK')
        self.assertEqual(json.loads(post.text)['status'], 'OK')
        self.assertEqual(json.loads(patch.text)['status'], 'OK')
        self.assertEqual(json.loads(put.text)['status'], 'OK')
        self.assertEqual(json.loads(delete.text)['status'], 'OK')
        self.assertEqual(head.text, '')

    def test_body_html_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/html')
        post = requests.post(f'http://{self.host}:{self.port}/post/html')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/html')
        put = requests.put(f'http://{self.host}:{self.port}/put/html')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/html')
        head = requests.head(f'http://{self.host}:{self.port}/head/html')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.headers['Content-Type'], 'text/html')
        self.assertEqual(post.headers['Content-Type'], 'text/html')
        self.assertEqual(patch.headers['Content-Type'], 'text/html')
        self.assertEqual(put.headers['Content-Type'], 'text/html')
        self.assertEqual(delete.headers['Content-Type'], 'text/html')

        self.assertEqual(get.text, '<html></html>')
        self.assertEqual(post.text, '<html></html>')
        self.assertEqual(patch.text, '<html></html>')
        self.assertEqual(put.text, '<html></html>')
        self.assertEqual(delete.text, '<html></html>')

    def test_body_css_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/css')
        post = requests.post(f'http://{self.host}:{self.port}/post/css')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/css')
        put = requests.put(f'http://{self.host}:{self.port}/put/css')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/css')
        head = requests.head(f'http://{self.host}:{self.port}/head/css')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.headers['Content-Type'], 'text/css')
        self.assertEqual(post.headers['Content-Type'], 'text/css')
        self.assertEqual(patch.headers['Content-Type'], 'text/css')
        self.assertEqual(put.headers['Content-Type'], 'text/css')
        self.assertEqual(delete.headers['Content-Type'], 'text/css')

        self.assertEqual(get.text, 'body {color: #fff}')
        self.assertEqual(post.text, 'body {color: #fff}')
        self.assertEqual(patch.text, 'body {color: #fff}')
        self.assertEqual(put.text, 'body {color: #fff}')
        self.assertEqual(delete.text, 'body {color: #fff}')

    def test_body_css_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/get/javascript')
        post = requests.post(f'http://{self.host}:{self.port}/post/javascript')
        patch = requests.patch(f'http://{self.host}:{self.port}/patch/javascript')
        put = requests.put(f'http://{self.host}:{self.port}/put/javascript')
        delete = requests.delete(f'http://{self.host}:{self.port}/delete/javascript')
        head = requests.head(f'http://{self.host}:{self.port}/head/javascript')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.headers['Content-Type'], 'text/javascript')
        self.assertEqual(post.headers['Content-Type'], 'text/javascript')
        self.assertEqual(patch.headers['Content-Type'], 'text/javascript')
        self.assertEqual(put.headers['Content-Type'], 'text/javascript')
        self.assertEqual(delete.headers['Content-Type'], 'text/javascript')

        self.assertEqual(get.text, 'const x = 10')
        self.assertEqual(post.text, 'const x = 10')
        self.assertEqual(patch.text, 'const x = 10')
        self.assertEqual(put.text, 'const x = 10')
        self.assertEqual(delete.text, 'const x = 10')

    def test_body_extra_response(self):
        plain_1 = requests.get(f'http://{self.host}:{self.port}/get/body/plain/extra/one')
        plain_2 = requests.get(f'http://{self.host}:{self.port}/get/body/plain/extra/two')
        plain_3 = requests.get(f'http://{self.host}:{self.port}/get/body/plain/extra/three')

        json_1 = requests.get(f'http://{self.host}:{self.port}/get/body/json/extra/one')
        json_2 = requests.get(f'http://{self.host}:{self.port}/get/body/json/extra/two')
        json_3 = requests.get(f'http://{self.host}:{self.port}/get/body/json/extra/three')

        self.assertEqual(plain_1.status_code, 200)
        self.assertEqual(plain_2.status_code, 200)
        self.assertEqual(plain_3.status_code, 200)

        self.assertEqual(json_1.status_code, 200)
        self.assertEqual(json_2.status_code, 200)
        self.assertEqual(json_3.status_code, 200)

        self.assertEqual(plain_1.text, "{'status': 'OK'}")
        self.assertEqual(plain_2.text, "{'status': 1000}")
        self.assertEqual(plain_3.text, "{'status': True}")

        self.assertEqual(json_1.text, '{"status": 100}')
        self.assertEqual(json_2.text, '"OK"')
        self.assertEqual(json_3.text, '"this is a test"')

if(__name__ == '__main__'):
    unittest2.main()