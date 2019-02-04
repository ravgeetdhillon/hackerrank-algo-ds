test=int(input())
while test!=0:
    n=int(input())
    data=[int(i) for i in input().split()]
    if n==1:
        print('YES')
    else:
        r_sum=0
        for i in data:
            r_sum+=i
        i=1
        l_sum=0
        r_sum-=data[0]
        flag=0
        while l_sum<=r_sum:
            if l_sum==r_sum:
                flag=1
                break
            else:
                l_sum+=data[i-1]
                r_sum-=data[i]
                i+=1
        if flag==1:
            print('YES')
        else:
            print('NO')
    test-=1
