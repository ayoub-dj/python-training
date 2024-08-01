# List Comprehension
list_comprehension = [[[f"E: {i}" if i % 2 == 0 else f"O: {i}" for i in range(3)] for _ in range(2)] for _ in range(2)]

# Dictionary Comprehension
keys = ['A', 'B', 'C', 'D', 'E', 'F']
values = [i+1 for i, _ in enumerate(keys)]
dict_comprehension = { k:f'Even {v}' for k,v in zip(keys, values) if v % 2 == 0 }

# Lambda
text = "Bad words are not allowed"
greeting = lambda name: f"Hello {name}" if name.lower() not in ['fuck', 'shit'] else text
remove_digits = lambda nums: ''.join(i for i in nums if not i.isdigit())

# Filter
def is_three_or_zero(n): return n == 3 or n == 0
seq = [0, 1, 2, 3, 5, 8, 13]
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [Person('Alice', 17), Person('Bob', 18), Person('Charlie', 19)]

filtered_people = list(filter(lambda person: person.age in range(18, 20), people))
get_even = filter(lambda n: not n % 2 != 0, seq)
get_three = filter(lambda n: is_three_or_zero(n), seq)
get_three_1 = filter(is_three_or_zero, seq)

# accumulate
from itertools import accumulate
nums = [1, 2, 100, 3, 4, 5, 99]
result = list(accumulate(nums, lambda a,b: a+b))

# Reduce
from functools import reduce
import operator
nums = [1, 2, 100, 3, 4, 5, 99]
maximum_number = reduce(lambda a, b: a if a > b else b, nums)
the_sum = reduce(operator.add, nums)

# Map
ls = ['Python', 'p', 'Django', 'Numpy', 'Pandas']
starts_with_p = map(lambda a: a if 'p' in a.lower() else 'Invalid', ls)
list_all = map(list, ls)

# Regular Expression (Regex)
import re
s = 'The django_rest@comcast.co is the best  ayoub@aol.com Django support-11@t-online.com python framework'
numbers = '(321) 456-7890 1 (983) 456-7890'
match = re.search(r"Django", s)
match_all = re.findall(r"[A-z0-9-]+@[A-z0-9-]+\.[A-z]{2,}", s)
match_compile = re.compile('[a-b]')
match_number = re.findall(r"\(\d{3}\)\s\d{3}\-\d{4}", numbers)

# re.split(' ', s)
# match_compile.findall(s)
# match.start() # Index
# match.end() # Index
# match.group() # Word
# match.span() # (start, end) Index

# recursion
def remove_duple(text):
    if len(text) <= 1: return text
    if text[0] != text[1]: return text[0] + remove_duple(text[1:])
    else: return remove_duple(text[1:])
    
remove_duple('dddjjjaaangggo')

# any
ls = ['Hello my name is @ jame']
# print(any('@' in i for i in ls))

# OOP
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def walk(self): pass

class Human:
    def __init__(self, name, protected_property, private_property, age=None):
        self.name = name
        self.age = age
        self._protected_property = protected_property
        self.private_property = private_property

    def __str__(self): return f"{self.name}"
    def ___private_method(self):
        # Do some things 
        return f"/{self.private_property}/"
    def get__private_method(self): return self.___private_method()
    def greeting(self): return f'Welcome {self.__str__()}'
    def walk(self): return 'I am walking'

class Employee(Human, Base):
    def __init__(self, name, protected_property, private_property, salary):
        self.salary = salary
        # Human.__init__(self, name)
        super().__init__(name, protected_property, private_property)

employee_1 = Employee("Maria", 'PROTECTED', "PRIVATE", "$5000")

# Operator Overloading in Python
class X:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __add__(self, z): return self.y + z.x

one, two = X(2, 1), X(9, 8)
# print(two.__add__(one))

# ITERABLES, ITERATORS and Generators
name = 'James'; toIterator = iter(name)
# print(next(toIterator))
# print(toIterator.__next__())
def generator_fun():
    yield "A"
    yield "B"
    yield "C"
# print(next(generator_fun()))

# Decorators
def not_allowed_name(func):
    def check_name(x):
        if x.lower() in ['fuck', 'shit']:
            print('Not Allowed name')

        func(x)
    return check_name

@not_allowed_name
def sayHello(xx):
    return f'Hello Master {xx}'

class IsInteger:
    def __init__(self, func): self.function = func

    def __call__(self, *args):
        if all([isinstance(i, int) for i in args]): return self.function(args)
        else: return "args cannot be a string !!"

@IsInteger
def get_even(*args): return args
# print(get_even(1, 2, 3, 5, 6, 7, 8))
# print(get_even(1, 2, 3, 5, '6', 7, 8))


# Static Methods, Static Methods, Class Methods
class J:
    count = 0
    ls = []
    def __init__(self, name) -> None:
        self.name = name
        J.ls.append(self)
    
    def __str__(self):
        return f'{self.name}'
    
    @staticmethod
    def calc_x_y(x, y):
        return x * y
    
    @classmethod
    def get_instance_count(cls):
        return f"We Have {len(cls.ls)} Instances From This Class"

j = J('James')
y = J('Dexter')


# Memory Management in Python
_2023 = 'I AM' # Create a new object in heap
_2024 = 'I AM' # This will check if the 'I AM' in heap, iF it is will take it, If not will create it

# print(id(_2023)) # 2174061443520
# print(id(_2024)) # 2174061443520
# print(id(_2024) == id(_2023))


# Testing in python
import unittest
class ClassForTesting(unittest.TestCase):
    def test_equal(self): self.assertEqual(1, 1, "Should be Equal")
    
    def test_not_equal(self): self.assertNotEqual(0, 5, "Should be not equal")

    def test_true(self): self.assertTrue(True, 'Should be true')

    def test_false(self): self.assertFalse(False, 'Should be false')

    def test_is(self): self.assertIs(False, False, "False is false")

    def test_is_not(self): self.assertIsNot(True, False, "True is not false")

    def test_is_none(self): self.assertIsNone(None, "Is none")

    def test_is_not_none(self): self.assertIsNotNone(1, "Is none")

    def test_in(self): self.assertIn(1, (7, 1, 23), '1 in iterable')

    def test_not_in(self): self.assertNotIn("M", ['A', 'L', 'X', 'B', 'W'], 'x not in iterable')

# if __name__ == "__main__":
#     unittest.main()


def get_sum(): assert 10 == 10, "Should Be 10"

def get_addition(): assert 10 + 1 == 11, "Should Be 11"

