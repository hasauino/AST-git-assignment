# List manager
from random import shuffle
from copy import copy


def random_order(list):
    '''returns the list with random order'''
    copied_list = copy(list)
    shuffle(copied_list)
    return copied_list


def order_by_increasing_value(list):
    '''returns the list ordered by increasing value'''
    copied_list = copy(list)
    copied_list.sort()
    return copied_list


def order_by_decreasing_value(list):
    '''returns the list ordered by decreasing value'''
    pass


def reverse_order(list):
    '''returns the list in reverse order'''
    pass


def stringfy_list(list):
    '''returns a list with all elements turned into strings'''
    pass


def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''
    pass


def get_highest_value(list):
    '''returns the highest value of the list'''
    pass


def get_lowest_value(list):
    '''returns the lowest value of the list'''
    pass
