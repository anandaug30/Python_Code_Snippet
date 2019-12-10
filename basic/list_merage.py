a = set(range(10))
b = set(range(3, 15))
e = set(range(15, 20))
print('set a: {}'.format(a))
print('list b: {}'.format(b))
c = set((*a, *b, *e))
d = *a, *b
print('set d: {}'.format(set(d)))
print('set c: {}'.format(c))
