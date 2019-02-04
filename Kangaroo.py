arr=[int(i) for i in input().split()]
a=arr[0]
b=arr[2]
difo=abs(b-a)
while True:
    arr[0]=arr[0]+arr[1]
    arr[2]=arr[2]+arr[3]
    difa=abs(arr[2]-arr[0])
    if difa>=difo:
        print('NO')
        break
    elif arr[0]==arr[2]:
        print('YES')
        break
    elif a>b and arr[2]>arr[0]:
        print('NO')
        break
    elif a<b and arr[2]<arr[0]:
        print('NO')
        break
