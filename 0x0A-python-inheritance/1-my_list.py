#!/usr/bin/python3
'''Module for MyList class.'''


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Sorted list printing method.'''
        print(sorted(self))
