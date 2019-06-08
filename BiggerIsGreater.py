def oneSwap(word):
    for i in range( len(word) - 1, 0, -1 ):
        for j in range( i-1, -1, -1 ):
            if ( word[i] > word[j] ):
                word[i], word[j] = word[j], word[i]
                save = j + 1
                return save
    return False

def biggerIsGreater(word):
    result = oneSwap(word)
    if not(result):
        print("no answer")
    else:
        word = word[:result] + word[result:len(word)][::-1]
        print( ''.join(word) )

tests = int(input())

for i in range(tests):
    word = list(input())
    biggerIsGreater(word)