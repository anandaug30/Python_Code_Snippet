import random
def sort_dutch_flag(dutch_flag):
    dummy_list = [0] * len(dutch_flag)
    red, green, white = 0, 0, 0
    for flag in dutch_flag:
        if flag == 0:
            red += 1
        elif flag == 1:
            green += 1
        elif flag == 2:
            white += 1

    for igreen in range(red, red + green):
        dummy_list[igreen] = 1

    for iwhite in range(red + green, len(dummy_list)):
        dummy_list[iwhite] = 2
    return dummy_list


dutch_flag = []
for i in range(100):
    dutch_flag.append(random.randint(0, 2))
print('unsort dutch flats {}'.format(dutch_flag))
#dutch_flag = [0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 0, 1]
print("sorted dutch flag {}".format(sort_dutch_flag(dutch_flag)))
