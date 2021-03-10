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
