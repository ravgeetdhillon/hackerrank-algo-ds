n=int(input())
cakes=[int(i) for i in input().split()]
dist=0
for i in range(n):
    dist+=(2**i)*max(cakes)
    cakes.remove(max(cakes))
print(dist)
