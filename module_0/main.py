import random

#generate random number from low to high
low = 1
high = 100
num = random.randint(low, high)

#binary search to guess number & count guesses
def computer_guess(num, low, high):
    count = 0
    guess = 0
    while guess != num:
        count += 1
        guess = (low+high)//2
        if guess > num:
            high = guess
        if guess < num:
            low = guess + 1
    print('The computer guessed {} from the {} time'.format(guess,count))

#launch computer guess function
computer_guess(num, low, high)
