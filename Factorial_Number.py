def numFac(n):
    if n==0:
        return (1)
    else:
        recurse=n*numFac(n-1)
        return (recurse)
print ('Hello User')
a=int(input("Type a number to know its factorial : "))
print('Factorial of',a,':',numFac(a))
e=input("Press Enter to exit")
