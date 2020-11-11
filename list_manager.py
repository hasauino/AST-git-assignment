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
    copied_list = copy(list)
    copied_list.sort(reverse=True)
    return copied_list


def reverse_order(list):
    '''returns the list in reverse order'''
    copied_list = copy(list)
    copied_list.reverse()
    return copied_list


def stringfy_list(list):
    '''returns a list with all elements turned into strings'''
    return [str(element) for element in list]


def multiply_list(list, multiple):
    '''returns the list with all elements multipled by the value multiple'''
    return [element*multiple for element in list]


def get_highest_value(list):
    '''returns the highest value of the list'''
    return max(list)


def get_lowest_value(list):
    '''returns the lowest value of the list'''
    pass
