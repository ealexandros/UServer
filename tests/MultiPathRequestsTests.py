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
        @cls.app.router.get('/*/*')
        def get(req, res):
            res.send('OK_TWO')

        @cls.app.router.post('/*/*')
        def get(req, res):
            res.send('OK_TWO')

        @cls.app.router.put('/*/*')
        def get(req, res):
            res.send('OK_TWO')

        @cls.app.router.patch('/*/*')
        def get(req, res):
            res.send('OK_TWO')

        @cls.app.router.delete('/*/*')
        def get(req, res):
            res.send('OK_TWO')

        @cls.app.router.head('/*/*')
        def get(req, res):
            res.send('OK_TWO')

        @cls.app.router.get('/*/*/*/*')
        def get(req, res):
            res.send('OK_FOUR')
        
        @cls.app.router.post('/*/*/*/*')
        def get(req, res):
            res.send('OK_FOUR')
        
        @cls.app.router.patch('/*/*/*/*')
        def get(req, res):
            res.send('OK_FOUR')
        
        @cls.app.router.put('/*/*/*/*')
        def get(req, res):
            res.send('OK_FOUR')

        @cls.app.router.delete('/*/*/*/*')
        def get(req, res):
            res.send('OK_FOUR')

        @cls.app.router.head('/*/*/*/*')
        def get(req, res):
            res.send('OK_FOUR')

        cls.app.start()

    def test_multi_path_redirection_depth_two(self):
        get = requests.get(f'http://{self.host}:{self.port}/1/2')
        post = requests.post(f'http://{self.host}:{self.port}/1/2')
        patch = requests.patch(f'http://{self.host}:{self.port}/1/2')
        put = requests.put(f'http://{self.host}:{self.port}/1/2')
        delete = requests.delete(f'http://{self.host}:{self.port}/1/2')
        head = requests.head(f'http://{self.host}:{self.port}/1/2')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, 'OK_TWO')
        self.assertEqual(post.text, 'OK_TWO')
        self.assertEqual(patch.text, 'OK_TWO')
        self.assertEqual(put.text, 'OK_TWO')
        self.assertEqual(delete.text, 'OK_TWO')
        self.assertEqual(head.text, '')

    def test_multi_path_redirection_depth_three(self):
        get = requests.get(f'http://{self.host}:{self.port}/1/2/3', headers={ 'Accept': None })
        post = requests.post(f'http://{self.host}:{self.port}/1/2/3', headers={ 'Accept': None })
        patch = requests.patch(f'http://{self.host}:{self.port}/1/2/3', headers={ 'Accept': None })
        put = requests.put(f'http://{self.host}:{self.port}/1/2/3', headers={ 'Accept': None })
        delete = requests.delete(f'http://{self.host}:{self.port}/1/2/3', headers={ 'Accept': None })
        head = requests.head(f'http://{self.host}:{self.port}/1/2/3', headers={ 'Accept': None })

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

    def test_multi_path_redirection_depth_four(self):
        get = requests.get(f'http://{self.host}:{self.port}/1/2/3/4')
        post = requests.post(f'http://{self.host}:{self.port}/1/2/3/4')
        patch = requests.patch(f'http://{self.host}:{self.port}/1/2/3/4')
        put = requests.put(f'http://{self.host}:{self.port}/1/2/3/4')
        delete = requests.delete(f'http://{self.host}:{self.port}/1/2/3/4')
        head = requests.head(f'http://{self.host}:{self.port}/1/2/3/4')

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, 'OK_FOUR')
        self.assertEqual(post.text, 'OK_FOUR')
        self.assertEqual(patch.text, 'OK_FOUR')
        self.assertEqual(put.text, 'OK_FOUR')
        self.assertEqual(delete.text, 'OK_FOUR')
        self.assertEqual(head.text, '')

    def test_multi_path_redirection_depth_five(self):
        get = requests.get(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        post = requests.post(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        patch = requests.patch(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        put = requests.put(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        delete = requests.delete(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        head = requests.head(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })

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

    def test_z_index_all_paths_star(self):
        @self.app.router.get('*')
        def get(req, res):
            res.send('OK_EVERYTHING')

        @self.app.router.post('*')
        def get(req, res):
            res.send('OK_EVERYTHING')
            
        @self.app.router.put('*')
        def get(req, res):
            res.send('OK_EVERYTHING')
            
        @self.app.router.patch('*')
        def get(req, res):
            res.send('OK_EVERYTHING')
            
        @self.app.router.delete('*')
        def get(req, res):
            res.send('OK_EVERYTHING')
            
        @self.app.router.head('*')
        def get(req, res):
            res.send('OK_EVERYTHING')

        get = requests.get(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        post = requests.post(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        patch = requests.patch(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        put = requests.put(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        delete = requests.delete(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })
        head = requests.head(f'http://{self.host}:{self.port}/1/2/3/4/5', headers={ 'Accept': None })

        self.assertEqual(get.status_code, 200)
        self.assertEqual(post.status_code, 200)
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(put.status_code, 200)
        self.assertEqual(delete.status_code, 200)
        self.assertEqual(head.status_code, 200)

        self.assertEqual(get.text, 'OK_EVERYTHING')
        self.assertEqual(post.text, 'OK_EVERYTHING')
        self.assertEqual(patch.text, 'OK_EVERYTHING')
        self.assertEqual(put.text, 'OK_EVERYTHING')
        self.assertEqual(delete.text, 'OK_EVERYTHING')
        self.assertEqual(head.text, '')
        
if(__name__ == '__main__'):
    unittest2.main()