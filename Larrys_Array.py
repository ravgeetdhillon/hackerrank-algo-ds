def checkAnswer(arr):
    for i in range(l - 1):
        if arr[i] + 1 != arr[i + 1]:
            return "NO"
    return "YES"

def rotate(i):
    flag = False
    while not( isFirstSmallest(i) ):
        arr.insert( i + 3, arr[i] )
        del arr[i]
        flag = True
    return flag

def isFirstSmallest(i):
    for a in range(i + 1, i + 3):
        if arr[i] > arr[a]:
            return False
    return True

tests = int( input() )
for _ in range(tests):
    l = int( input() )
    arr = [int(i) for i in input().split()]
    while True:
        i = 0
        flag = False
        while i < l - 2:
            if rotate(i):
                flag = True
            i += 1
        if not(flag):
                break

    print( checkAnswer(arr) )