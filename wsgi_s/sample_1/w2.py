#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Mar 8, 2016

@author: root
'''
import pprint

from paste.request import parse_formvars

def app(environ, start_response):
    fields = parse_formvars(environ)
    pprint.pprint(environ)
    print start_response
    if environ['REQUEST_METHOD'] == 'POST':
        start_response('200 OK', [('content-type', 'text/html')])
        return ['Hello ', fields['name'], '!']
    else:
        start_response('200 OK', [('content-type', 'text/html')])
        return ['<form method="POST">Name: <input type="text" ' \
                'name="name"><input type="submit"></form>']      
        
if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')   