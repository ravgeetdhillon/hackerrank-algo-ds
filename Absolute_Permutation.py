def displayPermutation(arr):
    for i in arr:
        print(i, end = ' ')
    print()

def createPermutation(n, k):
    arr = []
    for i in range(1, n + 1):
        if ( (i - 1) // k ) % 2 == 0:
            arr.append(i + k)
        else:
            arr.append(i - k)
    displayPermutation(arr)

tests = int( input() )
for _ in range(tests):
    parameters = [int(i) for i in input().split()]
    n = parameters[0]
    k = parameters[1]
    
    if k == 0:
        arr = [ i for i in range(1, n + 1) ]
        displayPermutation(arr)
    
    elif (n / k) % 2 == 0:
        createPermutation(n, k)
    
    else:
        print(-1)
