import math

# Speeding fine calculator
speed_limit = 55
speed = 100

if speed > speed_limit + 1 < 10:
    fine = 50
elif speed > speed_limit + 11 < 10:
    fine = 100
elif speed > speed_limit + 21:
    fine = 250
else:
    fine = 0

print(f"Fine: ${fine}")






# Leap year checker
year = 1990

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")






# Counting passing grades
grades = [88, 65, 72, 91, 54, 70]
passing = 70
counter = 0

passing = 70
for grade in grades:
    if grade >= passing:
       counter += 1
print(counter, "out of", len(grades), "students passed")





# Rocket launch countdown
lancher = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for rocket in lancher:
    if rocket == 0:
        print("Blastoff!")
        break 
    else:
        print(rocket)



#Temperature Converter
fahrenheit = 100
celsius = (fahrenheit / 9/5) + 32
print(f"{fahrenheit}°C is equal to {celsius}°F")


#Report Card
score = 84

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



#Password Checker

password = "csaea2026"
attempt = "CSAEA2026"


if attempt == password:
    print("Access granted")
else:
    print("Access denied")



# Roller Coaster Gate

height = 50
age = 8
has_adult = True

if height >= 48 and (age >= 10 or has_adult):
    print("May ride")
else:
    print("May not ride")



#Name Tag Generator

first = "Ada"
last = "Lovelace"
school = "CSAEA"

print(first + " " + last + " - " + school)




#Shopping Cart

cart = [12, 5, 30, 8]

total = 0

for price in cart:
    total = total + price

print("Items: " + str(len(cart)))
print("Total: $" + str(total))