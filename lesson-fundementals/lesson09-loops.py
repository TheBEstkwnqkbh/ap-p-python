# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.

import time

# The FOR-LOOP.
# A for-loop repeats for each element in a sequence (like a list or string).

animals = ["lamb", "sheep", "cow", "goose", "donkey"]

print("\nOur animals:", animals)

for a in animals:
    print("Now I'm petting a", a)
    # time.sleep(1) # pause for half a second

# We can loop a specific number of times using range().

for i in range(5): 
    print("Counting", i)

# range(start, stop, step)

for num in range(5, 105, 5):
    print(num)

# Strings are also iterable, so they can be looped as well!

fav_word = "Shennanigans"
print(fav_word)
letter_list = []

for letter in fav_word:
    print(letter)
    letter_list.append(letter + "!")

print(letter_list)

# Challenge 1: Sum Calculator
# Use a for-loop to find the sum of numbers from 1 to 10.
# ie, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# Expected output: 55

for nums in range(0, 10):
    