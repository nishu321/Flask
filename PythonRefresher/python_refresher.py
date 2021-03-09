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

# checks if both things are the same not just having same elements
print(friends is abroad)
print(friends is friends)

# If statements (already understand this section)

# in keyword (already understand this section)

# If statements with the "in" keyword 

