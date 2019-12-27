given_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


def diagonal_series_from_top_bottom(given_list, length):
    series = 0
    for i in range(0, length):
        j = i
        series += given_list[i][j]
    return series


def diagonal_series_from_bottom_top(given_list, length):
    series = 0
    j = length - 1
    for i in range(0, length):
        series += given_list[i][j]
        j -= 1
    return series


def diagonal_difference(arr):
    # Write your code here
    l_series, r_series = 0, 0
    length = len(arr)
    for i in range(0, length):
        j = i
        l_series += arr[i][j]
    j = length - 1
    for i in range(0, length):
        r_series += arr[i][j]
        j -= 1
    print(l_series, r_series)
    return l_series - r_series


#result = diagonal_series_from_top_bottom(given_list, 3) - diagonal_series_from_bottom_top(given_list, 3)
#print('difference diagonal matrix ', result)

print(diagonal_difference(given_list))