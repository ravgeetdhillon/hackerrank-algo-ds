s1=list(input())
s2=list(input())
delt=0
for i in s1:
    if i not in s2:
        delt+=1
    else:
        s1.remove(i)
        s2.remove(i)
for j in s2:
    if j not in s1:
        delt+=1
    else:
        s1.remove(j)
        s2.remove(j)
print(delt)
