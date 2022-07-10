# Guess the Number

##############################

##############################

# My program is to let the user guess a number between 1 and 30.

#############################


# Import random function
import random

# Count the number of attempts
attempt = 0

# Select a random number between 1-30
number = random.randint(1, 30)

print('Hello, what is your name?')
myName = input()

print('It is great to meet you,' + myName + '.')
print('I am thinkng of a number between 1 and 30')
print('Make a guess')

# user has 8 attempts to guess correctly
for attempt in range(8):
    myGuess = input()
    try:
        # check if the input is an integer
        myGuess = int(myGuess)
        # bound check
        if myGuess <= 0:
            print('Too low!, 1-30')
        if myGuess >= 31:
            print('Too High, 1-30')
        else:
            # Will notify user if their guess is out of range
            if myGuess < number:
                print('Your guess is too low.')
            elif myGuess > number:
                print('Your guess is too high.')
            elif myGuess == number:
                print("That's correct!")
                print('And it only took you' + str(attempt) + 'tries')
                break
# Not a number
    except ValueError:
        print('Sorry, that was not a number, try again.')
    attempt = attempt + 1
# When the user has gone beyond 8 guesses
if myGuess != number:
    print("You're out of guesses!, Try again.")
