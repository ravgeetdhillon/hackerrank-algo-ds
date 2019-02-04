def modulo_sum(array,var):
    sum=0
    for i in array:
        sum+=i
    return sum%var

test=int(input())
while test!=0:
    variable=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    max=0
    n=1
    while n<=variable[0]:
        i=0
        while (i+n)<=variable[0]:
            sub=arr[i:i+n]
            if max<modulo_sum(sub,variable[1]):
                max=modulo_sum(sub,variable[1])
            i+=1
        n+=1
    print(max)
    test-=1
