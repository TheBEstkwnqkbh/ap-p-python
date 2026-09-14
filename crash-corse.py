import math

# comment

# to comment multiple lines,
# highlight the lines,
# and click ctrl + / 

print("Hello world!")

# VARIABLE DECLARATIONS AND DATA TYPES:

a = 4           # integer 
b = 5.5         # float 
c = "CSAEA"     # string
d = False       # boolean 

print(a)
print(a, b, c, d)

# MATH OPERATORS 
# + - / *    %  **  //
# +=   -=   /=   

e = 3 - 1
print(e)
e += 20
print(e)

# f-string, formatted strings

print(f"e is equal to {e}")

e -= 7 
e += 12

print(f"e is NOW equal to {e}")

# COMPARISONS (booleans, which always return True of False)

#  <   >    <=   >=    ==    !=

print(5 <=  5)
print(7 == 4)
print(1 != 2)

isEqual = "Yes" != "YES"
print(isEqual)

# LOGICAL OPERATORS
# In order of precedence: not   and   or

f = False
t = True

#predict output before running code. 
print(not f) # True
print( f and t) #False
print(f or t) #True
print(f or t and not f) # True

# CASTING ()

g = int(5.6536539) # changes float to int
h = str(54) # changes int 54 to string "54"
print(g) # changes data type to int and chops off (truncates) everything after decimal

# STRINGS

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2+ s3 # concatenate with +
end += ", Cowboy."

print(end + "\n")

# MATH LIBRARY (import math at the top of the document)

print(math.sqrt(14))
print(math.ceil(3.65))
print(math.floor(8.94))
print(math.pow(2, 4))

# CONDITIONALS

# if    elif    else 

t = True
f = False

if f: 
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else: 
    print("Reached else")


if 1 > 1 and 1 == 1: 
    print("Reached the first condition")
elif 6 == 7 or 3 != 3:
    print("Reached second condition")
elif 10 != 10:
    print("Reached third condition")
else: 
    print("Reached else")

# LISTS
# A list can hold any type, and can grow or shrink at any time.

#index: 0   1   2   3   4
nums = [34, 52, 3, 64, 32]

print(nums)
print(nums[3]) #predict
print(nums[0])
print(nums[-1])
print(nums[-3])
print(nums[0] + nums[2])

nums[0] = 64
print(nums)

# LIST METHODS
# Special built-in methods

words = []

words.append("Word 1")
words.append("Word 2")
words.append("Word 3")
print(words)

words.remove("Word 1")
words.insert(0, "Word 4")
words[1] = "Word 5"
length = len(words)
print(words)
print(length)

# ITERATION

# For Loop
# A for loop will iterate over a RANGE.
# A range is a range of numbers. 
# # range(stop), range(start, stop), range( start, stop, step)
print()
for i in range(5):
    print(i)

animals = ["Sheep", "Deer", "Moose"]
print(f"List: {animals}")

for animal in animals:
    print(f"We saw {animal}")

nums = [5.1, 2.2, 5.3, 3.4, 8.5, 9.9]

# for n in nums:
#     print(n + 1)
#write a for loop to print each value in list nums

for i in range(len(nums)):
    print(nums[i])

# Debugging
print(len(nums))
print(range(5))

# for i in range(0,5):
#     print(nums[i])

# while loop

# iteratues while a condition is true
# when the condition becomes false, it stops

x = 1

while x <= 70:
    print(x)
    x+=1

f=False
t=True


while t or f:
    print(hi)

