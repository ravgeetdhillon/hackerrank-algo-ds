f = open("input.txt", "r")

parameters = [int(i) for i in input().split()]
n = parameters[0]
d = parameters[1]
data = [int(i) for i in input().split()]
# data = [int(i) for i in f.read().split()]
print(data)

modes = {}
for i in data[:d]:
    if i in modes:
        modes[i] += 1
    else:
        modes[i] = 1

mean = 0
for i in data[:d]:
    mean += i
mean = mean / d

notifications = 0
for p in range(d, n):
    mode_value = max( modes.values() )

    median, total = 0, 0
    for i in modes:
        if modes[i] == mode_value:
            median = median + i + (2 / 3) * (mean - i)
            total += 1
    
    median = median / total
    print(median, data[p])
    if data[p] >= median * 2:
        notifications += 1

    modes[ data[p - d] ] -= 1
    
    if data[p] in modes:
        modes[ data[p] ] += 1
    else:
        modes[ data[p] ] = 1
    
    mean = mean * d
    mean -= data[p - d]
    mean += data[p]
    mean = mean / d

print(notifications)