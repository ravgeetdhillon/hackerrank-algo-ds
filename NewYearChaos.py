def CheckChaos(arr):
    i=0
    for j in arr:
        pos=i-j+1
        if pos<-2:
            return -1
        i+=1

def CountBribes(arr,n):
    bribes=0
    for i in range(n):
        flag=0
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                bribes+=1
                flag=1
        if flag==0:
            return bribes
    return bribes

test=int(input())
while test!=0:
    n=int(input())
    queue=[int(i) for i in input().split()]
    if CheckChaos(queue)==-1:
        print('Too chaotic')
    else:
        print(CountBribes(queue,n))
    test-=1
