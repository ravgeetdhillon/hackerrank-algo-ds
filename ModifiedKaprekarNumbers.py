def isKaprekar(num):
    d = len( str(num) )
    save = num
    num = str(num ** 2)
    r = num[len(num) - d : ]
    l = num[ : len(num) - d]
    if l == '':
        l = 0
    if int(r) + int(l) == save:
        return True
    return False

a = int( input() )
b = int( input() )

answers = []
for num in range(a, b + 1):
    if isKaprekar(num):
        answers.append(num)

if len(answers) == 0:
    print("INVALID RANGE")
else:
    for num in answers:
        print(num, end=" ")