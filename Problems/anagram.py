"""Given two strings s1 and s2, check if both the strings are anagrams of each other.
Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.


Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams."""

from collections import Counter


def is_anagram(first_string, second_string):
    """ Implemented at basic level"""
    char_occur = 0
    if len(first_string) == len(second_string):
        for i in first_string:
            if first_string.count(i) == second_string.count(i):
                print("index of ", i, "is at FIRST string", first_string.index(i), " : ", first_string.count(i))
                print("index of ", i, "is at SECOND string", second_string.index(i), " : ", second_string.count(i))
            else:
                print("index of ", i, "is at FIRST string", first_string.index(i))
                print("index of ", i, "is at SECOND string", second_string.index(i))
                char_occur += 1
        if char_occur == 0:
            return True
        else:
            return False
    else:
        return False


def is_anagram_using_counter(first_string, second_string):
    cnt_first_string = Counter(first_string)
    cnt_second_string = Counter(second_string)

    if cnt_first_string == cnt_second_string:
        assert True, "Yes, its Anagram"
        #return True
    else:
        print(cnt_first_string, cnt_second_string)
        assert False, 'Not a Anagram'
        #return False


print(is_anagram('listen', 'silent'))
print(is_anagram('dad', 'bad'))
print(is_anagram_using_counter('listen', 'silent'))
print(is_anagram_using_counter('bad', 'dad'))
