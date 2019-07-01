import random
random.randint(1,5)
number = random.randint(1,5)
guess = 0
number == guess
while number != guess:
    guess = int(input("\n> "))

################################################################################
### This is a comment, what does the program do?
##import random
##number = random.randint(1,10)
##
##guess = 0
##
##while number != guess:
##    guess = input("Take a guess?\n> ")
##
##print("You got it!")
### Why does this loop never break?
### What happens if the indent is removed?
### What if guess is removed before the WHILE loop?
### How might we give the user hints?

################################################################################

##import random
##number = random.randint(1,10)
##guess = 0
##
##while number != guess:
##    guess = input("Take a guess?\n> ")
##    guess = int(guess)
##    if guess < number:
##        print("Too low")
##    if guess > number:
##        print("Too high")
##
##print("You got it!")
##
### Is it possible to get the input and cast to an int in one line of code?
### How might we make the problem harder now?
### How might we use binary search to solve this problem?
### Can we tell the user how many guesses it took them?

################################################################################

##import random
##number = random.randint(1,100)
##guess_cnt = 0
##
##while guess_cnt < 7:
##    guess_cnt += 1
##    guess = int(input("Take a guess?\n> "))
##    if guess < number:
##        print("Too low")
##    if guess > number:
##        print("Too high")
##    if guess == number:
##        break
##
##if guess == number:
##    print(f"You got it in {guess_cnt}.")
##else:
##    print(f"I was thinking of {number}.")
##
### How might the program be improved from here?

################################################################################
