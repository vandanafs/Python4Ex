fib_cache={}

def fib(n):
    if n<=1 :
        value=n
    elif n==2 :
        value=1
    elif n>2 :
         value=fib(n-1)+fib(n-2)

    fib_cache[n]=value
    return value


for n in range(1,31) :
    print(n,":", fib(n))
