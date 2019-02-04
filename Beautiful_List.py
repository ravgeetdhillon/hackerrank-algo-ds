t=int(input())
n=0
while n!=t:
    l=int(input())
    a=input()
    li=[int(i) for i in a.split()]
    p=[]
    for i in li:
        for j in li:
            if i==j:
                continue
            else:
                k=i*j
                if k not in p:
                    p.append(k)
    for e in p:
        if e not in li:
            print('no')
            break
        else:
            continue
    else:
        print('yes')
    n+=1
