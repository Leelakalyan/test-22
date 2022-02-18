def  isprime(n):
    for i in range(2,n):
        if n%i==0:
          return False
    return True

n=int(input('enter n:'))
sum=0
for i in range(2,n+1):
    if isprime(i):
        sum=sum+i
        print(i)

print('sum is:',sum)

Output:
enter n:
10
2
3
5
7
sum is: 17
