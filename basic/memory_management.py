"""	Understanding Memory management	a = 10,	my_obj = Custom_Class() 10
and my_obj are storied in stack memory
10( int class ) and Custom_class are storied in heap memory if a value changed to 11 ,
new object reference will be created ( ID (a) give us reference)
python follow references counter technique  collector
User weak.ref(obj_name) to check if object is dead or not
"""
import weakref


class Student:
    roll_id = None
    name = None
    age = None

    def __init__(self, roll_id, name, age):
        self.roll_id = roll_id
        assert isinstance(name, str)
        assert isinstance(roll_id, str)
        self.name = name
        assert isinstance(age, int)
        self.age = age

    def inform(self):
        print("student {} with roll number {} is {} old".format(self.roll_id, self.name, self.age))

    @staticmethod
    def information(cls):
        print("student {} with roll number {} is {} old".format(cls.roll_id, cls.name, cls.age))


print(10 * "# " + "Check Id for static method in a call" + 5 * " #")
print("Student class static method id {}:".format(id(Student.information(Student))))
print("-> Now notice, we didn't call static method but we try to see id of status method so it is executed")

print(10 * "# " + "Memory management with class objects " + 5 * " #")
std1 = Student('e405', 'anand', 24)
std1.inform()
std2 = Student('r34', 'raju', 22)
r = weakref.getweakrefs(std1)
c = weakref.getweakrefcount(std1)
print("Student Class object id {}".format(id(std1)))
print("Student Class object id {}".format(id(std2)))
print("Student class references is {} with count {}".format(r, c))

a = 10  # python is dynamic type , no need to of declare of variable type
b = 10  # same references  will be created which is same as a reference
c = a  # now a,b,c are in stack memory , value 10 in heap memory with same reference
print(10 * " #" + "lets see the ID values for all args" + 10 * "#")
print("reference of a {}".format(id(a)))
print("reference of d {}".format(id(b)))
print("reference of c {}".format(id(c)))
if id(a) is (id(a), id(b), id(c)):
    print('all ID are same')
print(10 * "#" + "lets try to change the value for a " + 10 * "#")
if id(a) is (a, b, c):
    print('all ID are same')
a = 11  # in heap memory,references of 11 will be assign to a
print("reference of a {}".format(id(a)))
print("reference of d {}".format(id(b)))
print("reference of c {}".format(id(c)))
b, c = 12, 12
print(10 * "#" + "now are seeing old references removed from heap, and new created " + 5 * "#")
print("reference of a {}".format(id(a)))
print("reference of d {}".format(id(b)))
print("reference of c {}".format(id(c)))
