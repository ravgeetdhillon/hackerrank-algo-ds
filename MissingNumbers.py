def Count_Num(num,arr):
    count=0
    for a in arr:
        if num==a:
            count+=1
    return count

l1=int(input())
arr1=[int(i) for i in input().split()]
l2=int(input())
arr2=[int(i) for i in input().split()]

stack=[]
miss=[]

for i in arr1:
    if i in stack:
        continue
    else:
        if Count_Num(i,arr1)!=Count_Num(i,arr2):
            miss.append(i)
        stack.append(i)

for i in arr2:
    if i in stack:
        continue
    else:
        miss.append(i)

while len(miss)!=0:
    print(min(miss),end=' ')
    miss.remove(min(miss))
