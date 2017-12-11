# Edgar Flores

# October 2, 2017

## Guess my number
import random
import math 
rounds = int(input(" How many numbers do you want to guess"))
total_error = 0
for i in range (rounds):
    random_number = random.randint(1,10)
    guess = int(input("Guess a number 1-10 :"))
    dif = abs(random_number - guess)
    print("The number was %d, and you guessed %d, for a difference of %d ." (random_number,guess, dif))
    total_errors += dif
avg = total_errors/ rounds
print( "Your total number of errors was %d ." % total_errors)
print("Your average was %f ." % avg)
if avg < 2:
    print("Were you reading my mind?")
elif avg < 3.5 :
    print("You  did alright")
elif avg < 4:
    print( "Don't gamble!")
    
