#### Data types
# 1. int -> doesnt have any decimal point
# 2. float -> has decimal point
# 3. str-> anything in quotes
# 4. bool-> true or false

#### Output and printing
print("Hello World") # Hello World
print(2+3) # 5
print(2.5+3.5) # 6.0
print("2"+"3") # 23
print('hello','end',87,False) # hello end 87 False

#### Variables
hello = "Hello"
saddan = "Saddan"

print(hello,saddan) # Hello Saddan
print(hello+saddan) # HelloSaddan
print(hello+" "+saddan) # Hello Saddan

hello_saddan= 'Hello Saddan' #in python use underscore to separate words instead of camel case

#### Input
# The output of input is always a string

input('What is your name? ') # What is your name? # user input
name = input('What is your name? ') # What is your name? # user input
print ('hello', name ,'you are awesome') # hello #user input# you are awesome

age_str = input('How old are you? ') # How old are you? # user input
print (age - 10) # TypeError: unsupported operand type(s) for -: 'str' and 'int'

# To fix this we need to convert the string to int
print (int(age_str) - 10)   
print (float(age_str) - 10
# or  
age_int = int(input('How old are you? ')) # How old are you? # user input
age_float = float(input('How old are you? ')) # How old are you? # user input
print (age_str - 10) 


#### Arithmetic operators
# Operands need to be same type
# order of operations are BEDMASM
# B -> Brackets, E -> Exponents, D -> Division, M -> Multiplication, A -> Addition, S -> Subtraction, M -> Modulus

x=9
y=3

result_add = x+y # 12
result_sub = x-y # 6
result_mul = x*y # 27
result_div = x/y # 3.0
result_mod = x%y # 0
result_exp = x**y # 729
result_floordiv = x//y # 3

#### String methods
# Strings are immutable
# Strings are ordered
# Strings are iterable
# you can stack methods

hello = 'Hello World'

print(hello[0]) # H
print(hello[1]) # e
print(hello.upper()) # HELLO WORLD
print(hello.lower()) # hello world
print(hello.capitalize()) # Hello world
print(hello.count('l')) # 3
print(hello.find('l')) # 2
print(hello.replace('World','Saddan')) # Hello Saddan
print(hello.split(' ')) # ['Hello', 'World']
print(hello.split('o')) # ['Hell', ' W', 'rld']
print(hello.split('o',1)) # ['Hell', ' World']

print(hello*3) # Hello WorldHello WorldHello World

print(hello.upper().count('l')) # 3


#### Conditionals operators
# == -> equal to
# != -> not equal to
# > -> greater than
# < -> less than
# >= -> greater than or equal to
# <= -> less than or equal to
# and -> both conditions need to be true
# or -> one of the conditions need to be true
# not -> reverse the condition
# not first , then and , then or


#### if statement

x= input('what is your name? ') # what is your name? # user input

if x == 'Saddan':
    print('Hello Saddan')
elif y == 'stranger':
    print('Hello stranger')
else:
    print('Hello World')

#### Lists
# Lists are mutable
# Lists are ordered
# Lists are iterable
# Lists can contain any data type

x= [1,2,3,4,5,6,7,8,9,10]
y=[4,True,'hi']

print(x[0]) # 1
print(x[1]) # 2
print(x[:3]) # [1, 2, 3]py
print(x[3:]) # [4, 5, 6, 7, 8, 9, 10]
print(x[0:3]) # [1, 2, 3]
print(x[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(x[0:10:2]) # [1, 3, 5, 7, 9]
print(x[0:10:3]) # [1, 4, 7, 10]

print(x+y) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, True, 'hi']

print(len(x)) # 10
x.append(11) 
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x.insert(0,0)
print(x) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x.remove(11)
print(x) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.pop()
print(x) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x.pop(0)
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
x.extend(y)
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, True, 'hi']
x.clear()
print(x) # []

a=[1,2,3]
b=a

a[0]=4
print(a) # [4, 2, 3]
print(b) # [4, 2, 3]

b=a.copy()
a[0]=9
print(a) # [9, 2, 3]
print(b) # [4, 2, 3]

#you can add lists inside a list
l=[1,2,3,[4,5,6]]

#### Tuples
# Tuples are immutable
# Tuples are ordered
# Tuples are iterable
# Tuples can contain any data type
# we cannot append, insert, remove, pop, clear, extend, or copy a tuple
# in short we can't change a tuple

x= (1,2,3,4,5,6,7,8,9,10)
y=(4,True,'hi')

#### for loop
# for loop will keep running until the condition is false

x= [1,2,3,4,5,6,7,8,9,10]

for i in range(10):
    print(i) # 0 1 2 3 4 5 6 7 8 9 (with new line)

for i in range(10,20):
    print(i) # 10 11 12 13 14 15 16 17 18 19 (with new line)

for i in range(10,20,2):
    print(i) # 10 12 14 16 18 (with new line)

for i in range(20,10,-2):
    print(i) # 20 18 16 14 12 (with new line)

for i in x:
    print(i) # 1 2 3 4 5 6 7 8 9 10 (with new line)

for i in range(len(x)):
    print(x[i]) # 1 2 3 4 5 6 7 8 9 10 (with new line)

for i,element in enumerate(x):
    print(i, element) # (0 1) (1 2) ... (with new line)

#### while loop
# while loop will keep running until the condition is false

x = 0
while x < 10:
    print(x)
    x += 1
#or

while True:
    print(x)
    x += 1
    if x == 10:
        break

#### sets
# sets are unordered
# sets are iterable
# sets can contain any data type
# sets are mutable
# sets are unique
# use when you only care about the existence of an element and not the order
# sets are faster than lists

x= {5,3,7,2,6}
y=set() # if you want to create an empty set
y={} # this will create an empty dictionary instead of an empty set
y{1,4,3,2}

print(x) # {2, 3, 5, 6, 7} note that the order is different
x.add(1) # {1, 2, 3, 5, 6, 7}
x.remove(1) # {2, 3, 5, 6, 7}
x.discard(1) # {2, 3, 5, 6, 7} if the element is not in the set, it will not throw an error
x.pop() # {3, 5, 6, 7} it will remove a random element
x.clear() # {} it will clear the set
x= {5,3,7,2,6}

print (12 in x # False
print (12 not in x) # True
print(x.union(y)) # {1, 2, 3, 4, 5, 6, 7} it will combine the two sets
print(x.intersection(y)) # {2, 3, 5, 6, 7} it will return the common elements
print(x.difference(y)) # {1} it will return the elements that are in x but not in y
print(x.symmetric_difference(y)) # {1, 4} it will return the elements that are in x or y but not in both

#### dictionaries
# dictionaries are unordered
# dictionaries are iterable
# dictionaries can contain any data type
# dictionaries are mutable

x= {'a':1, 'b':2, 'c':3}
y= dict() # if you want to create an empty dictionary
y= {} # this will create an empty dictionary

x['d']=4
print(x) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

x['a']=5
print(x) # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

print(x.keys()) # dict_keys(['a', 'b', 'c', 'd'])
print(x.values()) # dict_values([5, 2, 3, 4])
print(x.items()) # dict_items([('a', 5), ('b', 2), ('c', 3), ('d', 4)])
print(list(x.keys())) # ['a', 'b', 'c', 'd']
print(list(x.values())) # [5, 2, 3, 4]
print(list(x.items())) # [('a', 5), ('b', 2), ('c', 3), ('d', 4)]

del x['a']
print(x) # {'b': 2, 'c': 3, 'd': 4}

for key in x.keys():
    print(key) # b c d (with new line)

for key in x:
    print(key, x[key]) # b 2 c 3 d 4 (with new line)

for value in x.values():
    print(value) # 2 3 4 (with new line)

for key, value in x.items():
    print(key, value) # b 2 c 3 d 4 (with new line)

#### Comprehensions
# Comprehensions are a way to create lists, sets, and dictionaries in a single line of code

x=[i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x=[i for i in range(10) if i%2==0] # [0, 2, 4, 6, 8]
x=[i**2 for i in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
x=[i**2 for i in range(10) if i%2==0] # [0, 4, 16, 36, 64]
#you can also use it to create tuples, sets, and dictionaries

x=(i for i in range(10)) # <generator object <genexpr> at 0x0000020B0B0B0C50>
x=tuple(i for i in range(10)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
x={i for i in range(10)} # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


#### Functions
# Functions are a way to reuse code
# Functions are a way to organize code
# Functions are a way to make your code more readable
# Functions are a way to make your code more maintainable
# Functions are a way to make your code more scalable

def my_function():
    print('Hello World')

my_function() # Hello World

def my_function(name):
    print('Hello', name)

my_function('John') # Hello John

def my_function(name='John'):
    print('Hello', name)

my_function() # Hello John

def add (x,y):
    return x+y

print(add(1,2)) # 3

#### args and kwargs
# args and kwargs are used to pass a variable number of arguments to a function
# args is used to send a non-keyworded variable length argument list to the function 
# example: you do not know how many arguments will be passed to your function by the user so in this case you use args
# kwargs allows you to pass keyworded variable length of arguments to a function 
# example: you do not know how many keyword arguments will be passed to your function by the user so in this case you use kwargs


def random_function(x):
    def random_function2():
        print (x)
    return random_function2

print(random_function(5)())  # 5 None (with new line)

def func(x,y):
    pass

x=[1,23,253,545]

func(*x) # 1 23 253 545 unpacking the list

pairs= [('a',1), ('b',2), ('c',3)]
for pair in pairs:
    func(*pair) # a 1 b 2 c 3 (with new line) 

for pair in pairs:
    func(**{'a':5,'b':5}) # ('a', 1) ('b', 2) ('c', 3) (with new line)

def func2(*args,**kwargs):
    print(args)
func2(1,2,3,one=1) # (1, 2, 3) {'one': 1}

#### exceptions and error handling

raise FileExistsError('File already exists') # FileExistsError: File already exists

try:
    raise FileExistsError('File already exists')
except FileExistsError as e:
    print(e) # File already exists

try:
    x=7/0
except ZeroDivisionError as e:
    print(e) # division by zero
finally:
    print('This will always execute')


#### lambda functions
# lambda functions are a way to create anonymous functions
# lambda functions are a way to create functions in a single line of code
# lambda functions are a way to create functions without a name
# lambda functions are a way to create functions without a return statement

x= lambda a: a+10
print(x(5)) # 15

x= lambda a,b: a*b
print(x(5,6)) # 30

#### map and filter

x= [1,2,3,4,5,3,5,8,5,7]

y= list(map(lambda a: a+10, x))
print(y) # [11, 12, 13, 14, 15, 13, 15, 18, 15, 17]

y=map(lambda a: a+10, x)
print(y) # <map object at 0x0000020B0B0B0C50>

y= list(filter(lambda a: a%2==0, x))
print(y) # [2, 4, 8]

#### f strings
# f strings are a way to format strings
your_name= 'John'
x=f'hello {your_name} you are a{5+5}'

#### classes
# classes are a way to create objects
# classes are a way to create blueprints for objects
# classes are a way to create reusable code
# classes are a way to create objects that have attributes and methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() # Hello my name is John

#### inheritance
# inheritance is a way to create a new class from an existing class
# inheritance is a way to create a new class from an existing class and add new attributes and methods to it
# inheritance is a way to create a new class from an existing class and override existing attributes and methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.graduationyear)

x = Student("Mike", 10, 2019)
x.welcome() # Welcome Mike to the class of 2019

#### iterators
# iterators are a way to iterate over an object
# iterators are a way to iterate over an object using the next() method
# iterators are a way to iterate over an object using the iter() method

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) # <tuple_iterator object at 0x0000020B0B0B0C50>

print(next(myit)) # apple
print(next(myit)) # banana
print(next(myit)) # cherry

#### generators
# generators are a way to create iterators
# generators are a way to create iterators using the yield keyword
# generators are a way to create iterators using the next() method
# generators are a way to create iterators using the iter() method

def mygen():
    yield 1
    yield 2
    yield 3

x=mygen()
print(next(x)) # 1
print(next(x)) # 2
print(next(x)) # 3

#### decorators
# decorators are a way to add functionality to an existing function
# decorators are a way to add functionality to an existing function without modifying it
# decorators are a way to add functionality to an existing function without modifying it using the @ symbol

def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func

@my_decorator
def hello():
    print('hellooooo')

hello() # ********** hellooooo **********

#### modules
# modules are a way to create reusable code
# modules are a way to create reusable code using the import keyword
# modules are a way to create reusable code using the import keyword and the from keyword

import mymodule

mymodule.greeting("Jonathan") # Hello, Jonathan

import mymodule as mx

mx.greeting("Jonathan") # Hello, Jonathan

from mymodule import person1

print (person1["age"]) # 36

from mymodule import person1 as p1

print (p1["age"]) # 36

from mymodule import *

print (person1["age"]) # 36

