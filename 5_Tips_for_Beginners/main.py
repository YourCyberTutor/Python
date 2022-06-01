# YourCyberTutor - 5 Python Tips for Beginners
# PyCharm 2021.2.2 (Community Edition)
# Python 3.9.7

#Tip 1
name = "Bob"
number = 10
print("Hello "  + name +  "you entered the number " +  str(number))

# More efficient to use ,
print("Hello", name, "you entered the number",  number)

#Tip 2  - i is a variable and thus can be changed
#as you see all will print the same numbers
for i in range(0, 5):
    print(i)

for x in range(0, 5):
    print(x)

for number in range(0, 5):
    print(number)

#Tip 3 - functions in python
def myfun():
    x = 1
    y = 1
    total = x + y
    print(total)
myfun()

def myfun(x, y=0):
    total = x + y
    print(total)
myfun(1)

#Tip 4 - Rounding numbers
#This will divide and print the whole number with the remainder
x = 100 / 9
print(x)

# By using // will round the remainder and print a whole value
x = 100 // 9
print(x)
# Note you can also pass "round" prior to an action and will return the same value
x = 100 / 9
print(round(x))
# This will round the to second decimal place
print(round(x,2))


# Tip 5
''' If you looking to comment out multiple lines in python you can wrap in triple quotes 
In my comment
In my comment 
Pythons will not read anything encased and will contuine to the first python command'''
print("Not in my comment")

