n = int(input())
arr = [int(i) for i in input().split()]
arr.insert(0, '')
for i in range(1, n + 1):
    print(arr.index(arr.index(i)))
