def Sum(data,a,b):
    sum=0
    for i in range(a,b):
        sum+=data[i]
    return sum

test=int(input())
while test!=0:
    n=int(input())
    data=[int(i) for i in input().split()]
    flag=0
    start=0
    end=n-1
    mid=(start+end)//2
    save=0
    while save!=mid:
        save=mid
        l_sum=Sum(data,start,mid)
        r_sum=Sum(data,mid+1,end+1)
        if l_sum==r_sum:
            flag=1
            break
        elif l_sum<r_sum:
            mid+=1
        elif l_sum>r_sum:
            mid-=1
    if flag==0:
        print('NO')
    elif flag==1:
        print('YES')
    test-=1
