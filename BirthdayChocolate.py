l = int(input())
bar = [int(i) for i in input().split()]
parameters = [int(i) for i in input().split()]

days = parameters[0]
months = parameters[1]

count = 0
i = 0
while i + months <= len(bar):
    sub = bar[i: i + months]
    sum = 0
    for day in sub:
        sum += day
    if sum == days:
        count += 1
    i += 1

print(count)