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

#predict output. DOn't run!
print(not f) # True
print( f and t) #False
print(f or t) #True
print(f or t and not f) # True

# CASTING ()

g = int(5.6536539)
print(g)

# STRINGS

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2+ s3 # concatenation with +
end += ", Cowboy."

print(end + "\n")

# MATH LIBRARY

print(math.sqrt(14))
print(math.ceil(3.65))
print(math.floor(8.94))
print(math.pow(2,4))