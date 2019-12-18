num_list = [2, 3, 4, 5, 6]
result_list = list(x**2 for x in num_list)
print('square of the number in list {} are {}'.format(num_list, result_list))

print('print even number in given list {} are {}'.format(num_list,
                                                         list(x for x in num_list if x % 2 == 0)))