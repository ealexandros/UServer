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
            res.send('OK')
        
        @cls.app.router.post('/post')
        def post(req, res):
            res.send('OK')
            
        @cls.app.router.put('/put')
        def get(req, res):
            res.send('OK')
            
        @cls.app.router.patch('/patch')
        def patch(req, res):
            res.send('OK')
            
        @cls.app.router.delete('/delete')
        def delete(req, res):
            res.send('OK')

        @cls.app.router.head('/head')
        def head(req, res):
            res.send('OK')

        @cls.app.router.get('/this/is/t-_esre10t/aaa_1/')
        def get(req, res):
            res.send('OK')

        @cls.app.router.get('/')
        def head(req, res):
            res.send('OK')

        @cls.app.router.get('/param/:param')
        def param(req, res):
            res.send(req.url_param('param'))

        @cls.app.router.post('/param/:param')
        def param(req, res):
            res.send(req.url_param('param'))

        @cls.app.router.put('/param/:param')
        def param(req, res):
            res.send(req.url_param('param'))

        @cls.app.router.patch('/param/:param')
        def param(req, res):
            res.send(req.url_param('param'))
            
        @cls.app.router.delete('/param/:param')
        def param(req, res):
            res.send(req.url_param('param'))
            
        @cls.app.router.head('/param/:param')
        def param(req, res):
            res.send(req.url_param('param'))

        @cls.app.router.get('/testing', redirects=['/testing/redirects'])
        def get(req, res):
            res.send('OK_1')
            
        @cls.app.router.get('/second/testing', redirects=['/testing/1', '/testing/2', '/testing/3'])
        def get(req, res):
            res.send('OK_2')

        cls.app.start()

    def test_methods(self):
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

        self.assertEqual(get.text, 'OK')
        self.assertEqual(post.text, 'OK')
        self.assertEqual(patch.text, 'OK')
        self.assertEqual(put.text, 'OK')
        self.assertEqual(delete.text, 'OK')
        self.assertEqual(head.text, '')

    def test_methods_names(self):
        random_names = requests.get(f'http://{self.host}:{self.port}/this/is/t-_esre10t/aaa_1/')
        base = requests.get(f'http://{self.host}:{self.port}/')

        self.assertEqual(random_names.status_code, 200)
        self.assertEqual(base.status_code, 200)

        self.assertEqual(random_names.text, 'OK')
        self.assertEqual(base.text, 'OK')

    def test_redirects(self):
        redirect_1_1 = requests.get(f'http://{self.host}:{self.port}/testing')
        redirect_1_1 = requests.get(f'http://{self.host}:{self.port}/testing/redirects')

        redirect_2_1 = requests.get(f'http://{self.host}:{self.port}/second/testing')
        redirect_2_2 = requests.get(f'http://{self.host}:{self.port}/testing/1')
        redirect_2_3 = requests.get(f'http://{self.host}:{self.port}/testing/2')
        redirect_2_4 = requests.get(f'http://{self.host}:{self.port}/testing/3')

        self.assertEqual(redirect_1_1.status_code, 200)
        self.assertEqual(redirect_1_1.status_code, 200)
        self.assertEqual(redirect_2_1.status_code, 200)
        self.assertEqual(redirect_2_2.status_code, 200)
        self.assertEqual(redirect_2_3.status_code, 200)
        self.assertEqual(redirect_2_4.status_code, 200)

        self.assertEqual(redirect_1_1.text, "OK_1")
        self.assertEqual(redirect_1_1.text, "OK_1")
        self.assertEqual(redirect_2_1.text, "OK_2")
        self.assertEqual(redirect_2_2.text, "OK_2")
        self.assertEqual(redirect_2_3.text, "OK_2")
        self.assertEqual(redirect_2_4.text, "OK_2")

    def test_parameters(self):
        parameter = 'param_testing'
        get = requests.get(f'http://{self.host}:{self.port}/param/{parameter}')
        post = requests.post(f'http://{self.host}:{self.port}/param/{parameter}')
        patch = requests.patch(f'http://{self.host}:{self.port}/param/{parameter}')
        put = requests.put(f'http://{self.host}:{self.port}/param/{parameter}')
        delete = requests.delete(f'http://{self.host}:{self.port}/param/{parameter}')
        head = requests.head(f'http://{self.host}:{self.port}/param/{parameter}')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, parameter)
        self.assertEqual(post.text, parameter)
        self.assertEqual(patch.text, parameter)
        self.assertEqual(put.text, parameter)
        self.assertEqual(delete.text, parameter)
        self.assertEqual(head.text, '')

    def test_wrong_methods_ends(self):
        get = requests.get(f'http://{self.host}:{self.port}/post', headers={'Accept': None})
        post = requests.post(f'http://{self.host}:{self.port}/delete', headers={'Accept': None})
        patch = requests.patch(f'http://{self.host}:{self.port}/put', headers={'Accept': None})
        put = requests.put(f'http://{self.host}:{self.port}/patch', headers={'Accept': None})
        delete = requests.delete(f'http://{self.host}:{self.port}/head', headers={'Accept': None})
        head = requests.head(f'http://{self.host}:{self.port}/get', headers={'Accept': None})

        self.assertEqual(get.status_code, 500)
        self.assertEqual(post.status_code, 500)
        self.assertEqual(patch.status_code, 500)
        self.assertEqual(put.status_code, 500)
        self.assertEqual(delete.status_code, 500)
        self.assertEqual(head.status_code, 500)

        self.assertEqual(get.text, '')
        self.assertEqual(post.text, '')
        self.assertEqual(patch.text, '')
        self.assertEqual(put.text, '')
        self.assertEqual(delete.text, '')
        self.assertEqual(head.text, '')

    def test_wrong_methods_html_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/post', headers={ 'Accept': '*/*'})
        post = requests.post(f'http://{self.host}:{self.port}/delete', headers={ 'Accept': '*/*'})
        patch = requests.patch(f'http://{self.host}:{self.port}/put', headers={ 'Accept': '*/*'})
        put = requests.put(f'http://{self.host}:{self.port}/patch', headers={ 'Accept': '*/*'})
        delete = requests.delete(f'http://{self.host}:{self.port}/head', headers={ 'Accept': '*/*'})
        head = requests.head(f'http://{self.host}:{self.port}/get', headers={ 'Accept': '*/*'})

        self.assertEqual(get.status_code, 500)
        self.assertEqual(post.status_code, 500)
        self.assertEqual(patch.status_code, 500)
        self.assertEqual(put.status_code, 500)
        self.assertEqual(delete.status_code, 500)
        self.assertEqual(head.status_code, 500)

        self.assertNotEqual(re.search('^<!DOCTYPE html>', get.text.strip()), None)
        self.assertNotEqual(re.search('^<!DOCTYPE html>', post.text.strip()), None)
        self.assertNotEqual(re.search('^<!DOCTYPE html>', patch.text.strip()), None)
        self.assertNotEqual(re.search('^<!DOCTYPE html>', put.text.strip()), None)
        self.assertNotEqual(re.search('^<!DOCTYPE html>', delete.text.strip()), None)
        self.assertEqual(head.text, '')

    
    def test_wrong_methods_text_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/post', headers={ 'Accept': 'text/plain'})
        post = requests.post(f'http://{self.host}:{self.port}/delete', headers={ 'Accept': 'text/plain'})
        patch = requests.patch(f'http://{self.host}:{self.port}/put', headers={ 'Accept': 'text/plain'})
        put = requests.put(f'http://{self.host}:{self.port}/patch', headers={ 'Accept': 'text/plain'})
        delete = requests.delete(f'http://{self.host}:{self.port}/head', headers={ 'Accept': 'text/plain'})
        head = requests.head(f'http://{self.host}:{self.port}/get', headers={ 'Accept': 'text/plain'})

        self.assertEqual(get.status_code, 500)
        self.assertEqual(post.status_code, 500)
        self.assertEqual(patch.status_code, 500)
        self.assertEqual(put.status_code, 500)
        self.assertEqual(delete.status_code, 500)
        self.assertEqual(head.status_code, 500)

        self.assertEqual(get.text, 'GET not supported on /post path.')
        self.assertEqual(post.text, 'POST not supported on /delete path.')
        self.assertEqual(patch.text, 'PATCH not supported on /put path.')
        self.assertEqual(put.text, 'PUT not supported on /patch path.')
        self.assertEqual(delete.text, 'DELETE not supported on /head path.')
        self.assertEqual(head.text, '')

    def test_wrong_methods_json_response(self):
        get = requests.get(f'http://{self.host}:{self.port}/post', headers={ 'Accept': 'application/json'})
        post = requests.post(f'http://{self.host}:{self.port}/delete', headers={ 'Accept': 'application/json'})
        patch = requests.patch(f'http://{self.host}:{self.port}/put', headers={ 'Accept': 'application/json'})
        put = requests.put(f'http://{self.host}:{self.port}/patch', headers={ 'Accept': 'application/json'})
        delete = requests.delete(f'http://{self.host}:{self.port}/head', headers={ 'Accept': 'application/json'})
        head = requests.head(f'http://{self.host}:{self.port}/get', headers={ 'Accept': 'application/json'})

        self.assertEqual(get.status_code, 500)
        self.assertEqual(post.status_code, 500)
        self.assertEqual(patch.status_code, 500)
        self.assertEqual(put.status_code, 500)
        self.assertEqual(delete.status_code, 500)
        self.assertEqual(head.status_code, 500)

        self.assertRaises(TypeError, json.loads(get.text))
        self.assertRaises(TypeError, json.loads(post.text))
        self.assertRaises(TypeError, json.loads(patch.text))
        self.assertRaises(TypeError, json.loads(put.text))
        self.assertRaises(TypeError, json.loads(delete.text))
        self.assertEqual(head.text, '')

if(__name__ == '__main__'):
    unittest2.main()