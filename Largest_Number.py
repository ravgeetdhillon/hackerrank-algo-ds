num=int(input('How many numbers you want to input : '))
i=0
a=[]
while i!=num:
    t=int(input('Enter you number : '))
    a.append(t)
    i=i+1
print(a)
l=len(a)
n=0
temp=0
while n!=l:
    if temp<=a[n]:
        temp=a[n]
    else:
        temp=temp
    n=n+1
print(temp)
