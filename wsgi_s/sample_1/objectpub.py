#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Mar 8, 2016

@author: root
'''

from paste.request import parse_formvars
from paste.response import HeaderDict
import threading

webinfo = threading.local()

class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.fields = parse_formvars(environ)

class Response(object):
    def __init__(self):
        self.headers = HeaderDict(
            {'content-type': 'text/html'})
        
        
class ObjectPublisher(object):

    def __init__(self, root):
        self.root = root

    def __call__(self, environ, start_response):
        webinfo.request = Request(environ)
        webinfo.response = Response()
        
        obj = self.find_object(self.root, environ)
        response_body = obj(**dict(webinfo.request.fields))
        start_response('200 OK', webinfo.response.headers.items())
        return [response_body]
    
    def find_object(self, obj, environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            return obj
        
        path_info = path_info.lstrip('/')
        
        parts = path_info.split('/', 1)
        
        next = parts[0]
        
        if len(parts) == 1:
            rest = ''
        else:
            rest = '/' + parts[1]
        
        assert not next.startswith('_')
        next_obj = getattr(obj, next)
        environ['SCRIPT_NAME'] += '/' + next
        environ['PATH_INFO'] = rest
        return self.find_object(next_obj, environ)
    