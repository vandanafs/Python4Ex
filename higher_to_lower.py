from random import randrange
ran=randrange(1,101)
#print(ran)
maxTry=5

n=0
count=0
userGuess=0
while count!=maxTry:
    userGuess = int(input("Please enter number 1 to 100"))
    if(ran > userGuess) :
         print("your guess is too low ")
         count=count+1
         continue

    elif (ran< userGuess) :
         print("Your guess is too high")
         count=count + 1
         continue

    elif  (ran == userGuess) :
         print("Congrulations your guess is correct")
         break
    else :
         print("Please try some time later")


if(count == maxTry) :
    print("Oh sorry, your trial are over")