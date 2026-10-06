# Variables store any kind of information .
# Make sure to use descriptive variables names. 
# Note that variables can be overwritten

age = 73
print(age)
age = 74 
print(age)

password = "G00seberryPie5"
email = "mharrell@nhvweb.net"
print("Password:\t", password, "\nEmail:\t\t", email)

# variable name convention for booleans
isComplete = False
isEnabled = False
isAwake = True

# math conventions:
x = 3.14
y = 8
print(x + y)

# variables are flexible. you create or update another variable, like so:
count = 10 
print(count)
count_down = count - 1
print(count_down)
count = count_down
print(count)
count = count + count
print(count)

# Challenge 1: Rename Variables  
# Change the variable names x, y, z below to more descriptive names. 

x = "Radia Perlman"
y = 34
z = "Networking Engineer"

Name = x
Age = y
Occupation = z
print("Name:\t\t", Name, "\nAge:\t\t", Age, "\nOccupation:\t", Occupation)

# Challenge 2: Update Variables  
# Create a variable called 'count' with a value of 10.  
# Use another variable to increase 'count' by 5
# Print the result

count = 10
increase = 5
count = count + increase
print(count)

# Challenge 3: Swap Variables  
# Given variables num = 4 and y = "hello".  
# Swap the values so that x = "hello" and y = 4. 
# Use a temporary variable.  
# Hint: You will need to create one new variable. 

num = 4
y = "hello"
print("Before swap:\nnum:\t", num, "\ny:\t", y)
temp = num
num = y
y = temp
print("num:\t", num, "\ny:\t", y)
# Given variables num = 4 and y = "hello".  
# Swap the values so that x = "hello" and y = 4. 
# Use a temporary variable.  
# Hint: You will need to create one new variable. 