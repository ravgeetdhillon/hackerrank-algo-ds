n = int( input() )
lists = [ [] ]
for i in range(n//2):
    sub = input().split()
    if int(sub[0]) >= len(lists):
        for _ in range( int(sub[0]) - len(lists) + 1 ):
            lists.append([])
    lists[ int(sub[0]) ].append('-')

for i in range(n//2, n):
    sub = input().split()
    if int(sub[0]) > len(lists):
        for _ in range( int(sub[0]) - len(lists) + 1 ):
            lists.append([])
    lists[ int(sub[0]) ].append( sub[1] )

for i in lists:
    for j in i:
        print( j, end = ' ' )