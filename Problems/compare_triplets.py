# Complete the compareTriplets function below.
def compare_triplets(a, b):
    result_list = [0, 0]
    if len(a) is len(b):
        for i in range(0, len(a)):
            if a[i] > b[i]:
                result_list[0] += 1
            elif a[i] < b[i]:
                result_list[1] += 1
    return result_list

if '__name__' == '__main__':
    a = [17, 28, 30]
    b = [99, 16, 8]
    c = [5, 6, 7]
    d = [3, 6, 10]
    print(compare_triplets(a, b))
    print(compare_triplets(c, d))
