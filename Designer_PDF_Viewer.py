sizes = [int(i) for i in input().split()]
string = input()
max = 0
for char in string:
    height = sizes[ord(char) - ord('a')]
    if height > max:
        max = height

print( max * len(string) )