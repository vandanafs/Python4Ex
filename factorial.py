#num=int(input("please enter number to be factorized"))
from random import randrange
def fact(num) :

    if( num== 0 or num== 1) :
          return 1
    else :
        res=num * fact (num-1)

    return res

random_number=randrange(0,50)
print(random_number)
print(fact(random_number))