def staircase(n):
    for i in range(n + 1):
        print(" " * (n - i), "#" * i)


# staircase(6)


def sum_list_with_skip(given, index):
    result = 0
    for i in range(0, len(given)):
        if i != index:
            result += given[i]
    return result


a = [1, 2, 3, 4, 5]
print(sum_list_with_skip(a, 4))
