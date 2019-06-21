tests = int(input())

for _ in range(tests):
    string = list(input())

    save = 0
    dels = 0
    for i in range( save, len(string) - 1 ):
        if string[i] == string[i + 1]:
            # block += string[i]
            dels += 1
        else:
            save = i

    print(dels)