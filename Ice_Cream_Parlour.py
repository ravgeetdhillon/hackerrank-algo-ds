test=int(input())
while test!=0:
    done=0
    pool=int(input())
    flavours=int(input())
    cost=[int(i) for i in input().split()]
    n=0
    while n!=flavours:
        i=n+1
        while i!=flavours:
            if (cost[n]+cost[i])==pool:
                print(min(n,i)+1,max(n,i)+1)
                done=1
                break
            i+=1
        if done==1:
            break
        n+=1
    test-=1
