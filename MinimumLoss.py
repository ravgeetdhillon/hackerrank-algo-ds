n=int(input())
rate=[int(i) for i in input().split()]

min=max(rate)+1
for i in range(n):
    for j in range(i+1,n):
        if rate[i]>=rate[j] and rate[i]-rate[j]<min:
            min=rate[i]-rate[j]
print(min)
