#generate random number
import random
num = random.randint(1, 100)

#binary search to guess number & count guesses
def computer_guess(num):
    low = 1
    high = 100
    guess = 50
    count=0
    while guess != num:
        guess = (low+high)//2
        count+=1
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1
    print('The computer guessed {} from the {} time'.format(guess,count))

#launch computer guess function
computer_guess(num)