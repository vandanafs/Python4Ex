def fibno(n):
    if n<=1 :
        return n
    else :
        return  fibno(n-1) +fibno(n-2)

for n in range(1) :
    print(n,fibno(n))