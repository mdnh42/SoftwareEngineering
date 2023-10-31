
import random, math

lower = int(input("Enter lower Bound:- "))
upper = int(input("Enter Upper Bond:- "))

x = random.randint(lower, upper)
print("\n\tYou have only ", round(math.log(upper-lower+1, 2)), "chanches to guess the int!\n")

count = 0


while count<math.log(upper - lower + 1, 2):
    count+=1

    guess = int(input("Guess a number: - "))

    if x == guess:
        print("Congratulation you did it iin", count, "try")

        break 
    elif x>guess:
        print("You guessed too small")
    elif x < guess:
        print("you guessed too high")

if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d" %x )
    print("\tBetter luck next time!")