#!/usr/bin/python3
'''Module for inherits_from method.'''


def inherits_from(obj, a_class):
    '''For determining whether an object is truly a  subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
