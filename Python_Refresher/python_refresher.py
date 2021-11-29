#TEST2
# Section 2

# variables (already understand this section)

# string formatting
# f string
name = "Joe"
greeting = f"Hello, {name}"
print(greeting)

x = 1000

print(f"{x:,}")

# get input (already understand this section)

# write python first app
years = int(input("Enter your age:"))
months = years * 12

print(f"Your age, {years}, is equal to {months} months.")

# list, tuples, and sets (already understand this section)

# Advanced set operations
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)

print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)

print(both)

# Boolean in Python
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

# checks if both lists are the same not just having same elements
print(friends is abroad)
print(friends is friends)

# If statements (already understand this section)

# in keyword (already understand this section)

# If statements with the "in" keyword

# loops (already understand this section)

# list comprehensions
numbers = [1, 3, 5]
doubled = [number * 2 for number in numbers]

print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [name for name in friends if name.startswith("S")]

print(starts_s)

# Dictionaries (already understand this section)

# Destructuring variables
x, y = 5, 11

print(x, y)

# how to destruct a tuple
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist")]

for name, age, profession in people:
    print(f"{name} is {age} and works as a {profession}")

# if you want to ignore a part of the tuple
person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(f"{name} is a {profession}")

# separate list
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)


# functions (already understand this section)

# function arguments and parameters
def say_hello(name, surname):
    print(f"{name},{surname}")


# positional argument
say_hello("Bob", "Smith")

# keyword argument
say_hello(surname="Smith", name="Bob")

# mix argument type
# positional argument go first and any keyword argument go at the end
say_hello("Bob", surname="Smith")

# default function parameter values (already understand this section)

# Function returning values
# return by default return "none"
# return statement terminate function

# lambda functions
add = lambda num1, num2: num1 + num2

print(add(5, 7))

seq = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, seq)

print(list(doubled))

# dictionary comprehensions
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)


# unpacking function arguments
# pass in multiple arguments
def multiply(*args):
    print(args)
    total = 1

    for arg in args:
        total *= arg

    return total


print(multiply(1, 3, 5))


# pass in multiple arguments and one keyword argument
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided."


print(apply(1, 3, 6, 7, operator="*"))


# destruct multiple arguments
def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))


# keyword arguments
# return dict
def named(**kwargs):
    print(kwargs)


named(name="Bob", age="25")


# destruct kwargs
def named(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named(**details)


# loop through kwargs
def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age="25")


# Object - Oriented
# class is object blueprint
class Studnet():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg_grage(self):
        return sum(self.grades) / len(self.grades)


# create objects
student = Studnet("Rolf", (90, 90, 93, 78, 90))
student2 = Studnet("Rolf", (100, 90, 93, 78, 100))

print(student.avg_grage())
print(student2.avg_grage())


# Magic methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # print a string representation of the object
    def __str__(self):
        return f"This person {self.name}, {self.age} years old"

    # print an ambiguous representation of the object for programmers
    def __repr__(self):
        return f"<Person({self.name}, {self.age}"


bob = Person("Bob", 35)
print(bob)


# @classmethod and @staticmethod
class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    # Factory methods return class object ( similar to a constructor ) for different use cases.
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    # generally use static methods to create utility functions
    @staticmethod
    def static_method():
        print("Called static method")


test = ClassTest()
test.instance_method()

ClassTest.class_method()

ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}"

    @classmethod
    def hard_cover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)


book = Book.hard_cover("Harry Potter", 1500)
print(book)


# Class inheritance
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} {self.connected_by}"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capcity):
        super().__init__(name, connected_by)
        self.capcity = capcity
        self.remaining_pages = capcity

    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} pages remaining"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)


# multi level inheritance
class A:
    def f1(self):
        return "f1"

    def f2(self):
        return "f2"


class B(A):
    def f3(self):
        return "f3"

    def f4(self):
        return "f4"


class C(B):
    def f5(self):
        return "f5"

    def f6(self):
        return "f6"


# multiple inheritance
class A:
    def f1(self):
        return "f1"

    def f2(self):
        return "f2"


class B():
    def f3(self):
        return "f3"

    def f4(self):
        return "f4"


class C(A, B):
    def f5(self):
        return "f5"

    def f6(self):
        return "f6"


# class composition
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book1, book2)
print(shelf)


# type hinting
# tell what type the variable should be and tell what  the output type will be
def list_avg(seq: list) -> float:
    return sum(seq) / len(seq)


# list_avg(123)


# imports (already understand this section)

# Relative imports
# using . to import from current folder
# don't use relative imports just absolute

# errors in python
def divide(dividened, divisor):
    return dividened / divisor


grades = []

# finally always runs even if there is an error or not
# else only runs if the program passes the try
# put specific except to the top and general excepting to the bottom
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}")
finally:
    print("Thank You!")


# custom error handling
class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"

    def read(self, pages):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has "
                f"{self.page_count} pages")
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


book1 = Book("Python 101", 50)
try:
    book1.read(35)
    book1.read(50)
except TooManyPagesReadError as e:
    print(e)


# first class functions
# pass in a functions as a argument
def divide(dividened, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividened / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)

print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


try:
    print(search(friends, "Bob Smith", get_friend_name))
except RuntimeError as e:
    print(e)

# Mutability in python
a = []
b = a

a.append(35)

print(a)
print(b)


# Mutable default parameters
# bad to use mutable types for default parameter
class Students:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Students("Bob")
rolf = Students("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
