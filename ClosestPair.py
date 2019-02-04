n=int(input())
queue=[int(i) for i in input().split()]

min=abs(queue[0]-queue[1])
num=[]
for i in range(n):
    for j in range(i+1,n):
        if abs(queue[i]-queue[j])<min:
            num=[]
            num.append(queue[i])
            num.append(queue[j])
            min=abs(queue[i]-queue[j])
        elif abs(queue[i]-queue[j])==min:
            num.append(queue[i])
            num.append(queue[j])

n=len(num)
for i in range(n):
    for j in range(n-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            
for i in num:
    print(i,end=' ')
