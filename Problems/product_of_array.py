"""
Given an array nums of n integers where n>1 , return an array output such that output[i] is
equal to product of all the element of nums except num[i]
input: [1,2,3,4]
output : [24,12,8,6]
"""
from functools import reduce


def product_of_list_number(given_list):
    """
    product of given array
    :type given_list: object
    """
    result_list = list()
    right_list = [1]*len(given_list)
    left_list = [1]*len(given_list)
    print(given_list)
    for i in range(1, len(given_list)):
        right_product = reduce(lambda x, y: x * y, given_list[i:])
        right_list[i-1] = right_product
    print(right_list)
    for i in range(1, len(given_list)):
        left_product = reduce(lambda x, y: x * y, given_list[0:i])
        left_list[i] = left_product
    print(left_list)
    for i in range(len(given_list)):
        result_list.append(right_list[i] * left_list[i])
    print(result_list)
    print(list(map(lambda x, y: x*y, left_list, right_list)))


input_list = [4, 2, 3, 4]
product_of_list_number(input_list)
