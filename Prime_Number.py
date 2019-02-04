ok=('y')
a=19
for i in range(2,a):
    if a%i==0:
        ok=('n')
        break
if ok=='n' and a%2==0:
    print('Not a prime number.')
else:
    print('Prime Number.')
