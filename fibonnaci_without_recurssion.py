num=input("Please enter the number to which you want to see fibonaci series")
#5
f0=1
f1=1
print(f0)
print(f1)
fibprev=f1;
fibprev2=f0;
for n in range(2,int(num)):
     fib= fibprev+fibprev2;
     print(fib)
     fibprev2 = fibprev
     fibprev=fib

print('The final fib value '+str(fib))





