def isSorted(arr):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def getLeft():
    for i in range(n - 1):
        if arr[i + 1] < arr[i]:
            l = i
            break
    else:
        return "sorted"
    return l

def getRight():
    for i in range(n - 1, 0 , -1):
        if arr[i - 1] > arr[i]:
            r = i
            break
    else:
        return "sorted"
    return r

def checkSwap():
    arr1 = arr[:]
    arr1[l], arr1[r] = arr1[r], arr1[l]
    if isSorted(arr1):
        return True
    return False

def checkReverse():
    arr1 = arr[:l] + arr[l : r + 1][::-1]
    try:
        arr1 += arr[r + 1:]
    except:
        pass
    if isSorted(arr1):
        return True
    return False

n = int( input() )
arr = [ int(i) for i in input().split() ]

l = getLeft()
r = getRight()

if l < r:
    swap = checkSwap()
    if not(swap):
        reverse = checkReverse()
        if not(reverse):
            print("no")
        else:
            print("yes")
            print( "reverse", l + 1, r + 1 )
    else:
        print("yes")
        print( "swap", l + 1, r + 1 )
else:
    print("no")