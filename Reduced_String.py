inp='abbcccd'
li=[char for char in inp]
n=0
r=[]
while n<len(li)-1:
    if li[n]==li[n+1]:
        n+=2
    else:
        r.append(li[n])
        n+=1
print(str.join(r,'-'))
