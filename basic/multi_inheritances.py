class A:
    @staticmethod
    def first_fn(message):
        print('message from class A -> {}'.format(__name__, message))


class B:
    def __init__(self, a):
        print(a)

    def second_fn(self, message):
        print(self.__class__)
        print('message from class {} -> {}'.format(__class__, message))

class C(A,B):
    def first_fn(message):
        print('this is from class c')

A.first_fn('from anand')
B('a').second_fn('check this one')
C.second_fn(B,'ss')
C.first_fn('ss')