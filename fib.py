def fib(n):
    if n<=0:
        exit('n must be >=0')
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

result =[]
for i in range(1,11):
    result.append(fib(i))
print result