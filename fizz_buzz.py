
print(" Print numbers 1 to 100" )
for n in range(1,101):
     if (n % 3 == 0 and   n % 5 == 0):
         print(str(n) + " FizzBuzz")

     elif n % 5 == 0 :
         print(str(n)+" Buzz")

     elif (n % 3 == 0 ):
         print(str(n) + " Fizz")
     else :
         print( "The number "+str(n))
