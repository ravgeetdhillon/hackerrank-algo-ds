score=[int(i) for i in input().split()]
n=1
counth=0
countl=0
temph=score[0]
templ=score[0]
while n!=len(score):
    if score[n]>temph:
        counth+=1
        temph=score[n]
    elif score[n]<templ:
        countl+=1
        templ=score[n]
    else:
        pass
    n+=1
print(counth,countl)
