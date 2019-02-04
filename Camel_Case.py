import string
a='meIamGoodBoy'
s=''
for char in a:
    if str.isupper(char)!=True:
        s=s+char
    elif str.isupper(char)==True:
        print(s)
        s=char
print(s)
