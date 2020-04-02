n = int(input())
arr = [int(i) for i in input().split()]
records = {}
for i in arr:
    if i in records:
        records[i] += 1
    else:
        records[i] = 1

print( n - max(records.values()) )