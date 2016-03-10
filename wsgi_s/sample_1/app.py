#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Mar 9, 2016

@author: root
'''

from objectpub import ObjectPublisher
from middleware import AuthMiddleware

class Root(object):

    # The "index" method:
    def __call__(self):
        return '''
        <form action="welcome">
        Name: <input type="text" name="name">
        <input type="submit">
        </form>
        '''
    def a(self):
        pass

    def welcome(self, name):
        return 'Hello %s!' % name

app = ObjectPublisher(Root())
wrapped_app = AuthMiddleware(app)

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(wrapped_app, host='127.0.0.1', port='8080')