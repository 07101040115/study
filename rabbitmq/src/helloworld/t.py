#! /usr/bin/env python


def foo(a, b, c=1, *arg,  **kargs):
    print a
    print b
    print c
    print arg
    print kargs
    
    
foo(1,2,3,4,5, x=1, y=2)
    
    