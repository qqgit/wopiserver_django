#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018-2-10

@author: qi
'''

from django.test import TestCase, tag
import requests, json
from wopiserver_django import settings
import os
from io import BytesIO
from datetime import datetime

# tests for wopi get-file-info, 
class WOPITest(TestCase):
    @tag('client')
    def test_client_wopi_get_file_info(self):
        response = self.client.get('/wopi/files/test.txt')
        self.assertEqual(response.status_code, 200)
    @tag('client')
    def test__client_wopi_get_file_content(self):
        response = self.client.get('/wopi/files/test.txt/contents')
        self.assertEqual(response.status_code, 200)
    
    @tag('requests')
    def test_requests_wopi_get_file_info(self):
        fileid = 'test.txt'
        response = requests.get('http://127.0.0.1:8000/wopi/files/{fileid}'.format(fileid=fileid))
        self.assertEqual(response.status_code, 200)
        self.assertEqual( json.loads(response.content)['BaseFileName'], fileid)
    @tag('requests')
    def test__requests_wopi_get_file_content(self):
        fileid = 'test.txt'
        response = requests.get('http://127.0.0.1:8000/wopi/files/{fileid}/contents'.format(fileid=fileid))
        self.assertEqual(response.status_code, 200)
        file_path = os.path.join(settings.WOPI_FILE_DIR,'test.txt')
        self.assertTrue(os.path.exists(file_path))
        with open(file_path,'rb') as f:
            self.assertEqual(response.content ,f.read())
    @tag('requests')
    def test__requests_wopi_post_file_content(self):
        dt = datetime.now() 
        fileid = 'test_byte.txt'
        b= BytesIO()
        b.write('中文bytes, Time:{dt}'.format(dt=dt.strftime('%Y-%m-%d %H:%M:%S %f')).encode('utf-8'))
        response = requests.post('http://127.0.0.1:8000/wopi/files/{fileid}/contents'.format(fileid=fileid), data=b.getvalue())
        self.assertEqual(response.status_code, 200)
        file_path = os.path.join(settings.WOPI_FILE_DIR,fileid)
        self.assertTrue(os.path.exists(file_path))
        with open(file_path,'rb') as f:
            fr = f.read()
            bv = b.getvalue()
            print('bv: {bv}'.format(bv=bv))
            print('fr: {fr}'.format(fr=fr))
            self.assertEqual(bv ,fr)