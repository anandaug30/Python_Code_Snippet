from functools import lru_cache


def recursive_fibonacci_number(n):
    """" basic Fibonacci number function"""
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return recursive_fibonacci_number(n - 1) + recursive_fibonacci_number(n - 2)


fibonacci_cache = {}


def recursive_fibonacci_number_cache(n):
    """
     implementing memoization explicitly
     if we have cached the value, then return it 0
    """
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # compute the Nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = recursive_fibonacci_number_cache(n - 1) + recursive_fibonacci_number(n - 2)
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


@lru_cache(maxsize=1000)
def recursive_fibonacci_number_lru(n):
    """Implement memorization using LRU"""
    if type(n) != int:
        raise TypeError("n must be a integer, provided {}".format(n))
    if n < 1:
        raise TypeError("n must be a positive integer")
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return recursive_fibonacci_number_lru(n - 1) + recursive_fibonacci_number_lru(n - 2)


"""
# using basic Fibonacci number
for number in range(1, 39):
    #print(number, ";", recursive_fibonacci_number_cache(number))
    print(recursive_fibonacci_number(number+1)/recursive_fibonacci_number(number))

# using explict memo
for number in range(1, 39):
    print(number, ";", recursive_fibonacci_number_cache(number))
    print(recursive_fibonacci_number_cache(number+1)/recursive_fibonacci_number_cache(number))
"""
# using functool lru_cache
for number in range(1, 500):
    print(number, ";", recursive_fibonacci_number_lru(number))
    # print(recursive_fibonacci_number_lru(number+1)/recursive_fibonacci_number_lru(number))
