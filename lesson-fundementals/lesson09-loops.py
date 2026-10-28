# # LOOPS IN PYTHON
# # Loops repeat a block of code until they hit a limit or condition.
# # They exist to save us from typing the same line 500 times.
# # Python gives us for-loops and while-loops.

# import time

# # The FOR-LOOP.
# # A for-loop repeats for each element in a sequence (like a list or string).

# animals = ["lamb", "sheep", "cow", "goose", "donkey"]

# print("\nOur animals:", animals)

# for a in animals:
#     print("Now I'm petting a", a)
#     # time.sleep(1) # pause for half a second

# # We can loop a specific number of times using range().

# for i in range(5): 
#     print("Counting", i)

# # range(start, stop, step)

# for num in range(5, 105, 5):
#     print(num)

# # Strings are also iterable, so they can be looped as well!

# fav_word = "Shennanigans"
# print(fav_word)
# letter_list = []

# for letter in fav_word:
#     print(letter)
#     letter_list.append(letter + "!")

# print(letter_list)

# # Challenge 1: Sum Calculator
# # Use a for-loop to find the sum of numbers from 1 to 10.
# # ie, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# # Expected output: 55
# # initialize a variable to hold the total
# print()
# total = 0
# for i in range(1,11):
#     total = total + i

# print(total)

# # A while-loop repeats *while* a condition is true.
# # If you forget to change the condition, it loops forever.
# # And then your program becomes immortal. Avoid that.

# # += to add to a variable, -= to subtract to a variable, = to overright 

# count = 0 

# while count < 5:
#     print(f"Loopin' -- We are on loop index # {count}")
#     count += 1
#     time.sleep(0.5)

# # Example with user input 

# user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to escape")

# # Loop Control Statements
# pass 
# for i in range(1,11):

#     if i == 3: 
#         print("Skipping 3")
#         continue # skips this iteration
#     if i == 6:
#         print("Breaking at 6")
#         break # stop the loop entirely
#     if i == 9:
#         pass # place holder. does nothing. will code in the future

#     print("Number", i)

# # # Challenge 2: Guess Until Correct
# # # Create a while-loop that keeps asking for a number until the user types 7.
# # #H int: Take the user input within the loop, so it asks for a guess each time!

# user_number = 0
# while user_number != 7:
#     user_number = int(input("Guess the number: "))
# print("You guessed it!")

# # Challenge 3: Use a whiteboard to predict (no running!). Write the output, then check.
# for i in range(10, 0, -3):
#     print(i)

# for i in range(3):
#     if i == 5:
#         break
#     else:
#         print("done")


# # Challenge 4: Trace. Track total and n each pass. What prints?
# total = 0
# n = 1

# while total < 20:
#     total = total + n
#     n += 2

# print(total, n)

# # Example:
# # Pass 1: check 0 < 20 → True
# #         total = 0 + 1 = 1
# #         n = 1 + 2 = 3
# # Pass 2: check 1 < 20 → True
# #         total = 1 + 3 = 4
# #         n = 3 + 2 = 5


# # Challenge 3: This code should print the number of vowels in "pineapple".
# # But this code has bugs, and is in the wrong order. 
# # Unscramble to count vowels in "pineapple". One line doesn't belong.
# # 
# #       count += 1
# #     count = 0
# #     print(count)
# #     for letter in "pineapple":
# #         if letter in "aeiou":
# #             count = 1



# count = 0
# for letter in "pineapple":
#     if letter in "aeiou":
#         count += 1
# print(count)






# # # Challenge 4: Solve on whiteboard first Debug. 
# # # This loop never ends! Press Ctrl+C to stop it.
# # # Fix it by only changing only one small thing.

# n = 10
# while n != 0:
#     n -= 3
# print("Escaped!")

# Challenge 5: Write a guessing game with 5 tries and hints.
# The computer picks a secret number from 1 to 20. The player gets 5 guesses.
# The player will receive HINTS if they have an incorrect guess.
#
# preconditions: 
# the random library; 
# a random integer stored as the 'secret' that the player must guess.
#
# Pseudocode:
#   repeat 5 times (use a for-loop with range):
#       ask the player for a guess (convert it to an int!)
#       if guess equals secret → print "Got it!" and stop the loop
#       otherwise, if guess is bigger → print "Too high"
#       otherwise → print "Too low"
#   if the loop never stopped early → print "Out of guesses! It was" + secret

import random
secret = random.randint(1, 20)

for i in range(5):
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Got it!")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
else:
    print("Out of guesses! It was", secret)
