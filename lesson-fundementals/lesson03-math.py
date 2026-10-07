#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

from cmath import pi


add = 743543 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 7 / 2
print("Float division:", float_divide)

integer_divide = 7 // 2
print("Integer division:", integer_divide)

mod = 7 % 2
print("Modulus: ", mod) 

exponent = 7 ** 2
print("Exponent:", exponent)

#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result:", result3)

print("\n")
# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  

width = 8 
hight = 5
result = hight * width
print(result)

print("\n")
# Create separate variables for width, height, and result. Print result. 

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  
# Separate variables for pi, radius, and result. 

pi = 3.14
radius = 7
result = pi *radius ** 2
print(result)

print("\n")
# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  
# Print the result in this format: 
#     Book: <$ cost of book>
#     Notebook: <$ cost of notebook>
#     Total: <$>

book = 12.99
notebook = 3.50
book_total = book * 3
notebook_total = notebook * 4
shopping_total = book_total + notebook_total

print(f"Book:\t\t${book_total:.2f}" f"\nNotebook:\t${notebook_total:.2f}" f"\nTotal:\t\t${shopping_total:.2f}")
print("\n")
# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 

num = 57

if num % 2 == 0:
    print("Even")
else:
    print("Odd")