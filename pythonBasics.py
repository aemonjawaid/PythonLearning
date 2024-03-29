
print("Hello World!")

# variables
price = 12.3
first_name = "Aemon"
is_online = False
print("Hello: " + first_name)

# take input
name = input("Enter your name: ")
print(name)

# type conversion
birth_year = input("Enter birth year: ")
age = 2024 - int(birth_year)
print(age)

# strings
course = "Learning Python"
print(course.find("Python"))
print("Python" in course)

# arithmetic operators
# // -> gives whole number
print(10 // 4)
# ** -> use for power
print(2 ** 3)

# if else condition
temperature = 20
if temperature > 30:
    print("It is a hot day")
elif temperature > 20:
    print("Something")
print("Done")

# while loop
j = 1
while j <= 5:
    print(j)
    j = j + 1

# Lists
names = ["John", "Doe", "Albert", "Rio"]
names[0] = "Jane"
names.insert(4, "Sara")
print(names[0:3])  # it will exclude last index and print variables from 0...2
print("Sara" in names)

# for loop
foodItems = ["Burger", "Pizza", "Pasta"]
for item in foodItems:
    print(item)

# range
wholeNumbers = range(5)
oddNumbers = range(1, 10, 2)
for oddNo in oddNumbers:
    print(oddNo)

# tuples -> immutable lists
immutableList = (1, 2, 3, 4, 5)
