def sum_list_with_skip(given, index):
    result = 0
    for i in range(0, len(given)):
        if i != index:
            result += given[i]
    return result


def mini_max_sum(arr):
    sum_list = list()
    for i in range(0, len(arr)):
        sum_list.append(sum_list_with_skip(arr, i))
    print(min(sum_list), max(sum_list))


def sum_list(given):
    result = 0
    for i in given:
        result += i
    return result


