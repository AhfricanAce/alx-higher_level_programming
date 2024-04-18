#!/usr/bin/python3
'''Module for is_same_class method.'''


def is_same_class(obj, a_class):
    '''For determining whether an object is an instance or a class.'''
    return type(obj) == a_class
