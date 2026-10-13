import random
# USER INPUT IN PYTHON
#print("<PROMPT>")
# print()

name = input("Enter your name: ")
print(f"Hello {name}")

print(type(name))

age = input("Enter your age: ")
print(f"Your age is {age}")

print(type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Enter your height: "))
print(f"You are {height} meters tall")
print(height + 1)

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

favorite_color = input("What is your favorite color? ")
print(f"Your favorite color is {favorite_color}")


# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = number1 + number2
print(f"The sum of {number1} and {number2} is {result}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 

diameter = float(input("Enter the diameter of the circle: "))
radius = diameter / 2
area = 3.14 * radius ** 2
print(f"The area of the circle is {area}")

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

sides = int(input("How many sides should the die have? "))

roll = random.randint(1, sides)
print(f"You rolled a {roll} on a {sides}-sided die.")