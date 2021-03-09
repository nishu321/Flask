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