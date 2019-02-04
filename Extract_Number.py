numbers=['0','1','2','3','4','5','6','7','8','9']
print('***PROGRAM : To extract the valid phone number from the string***')
a=str(input('Input your string : '))
p=''
for char in a:
    if char in numbers:
        p=p+char
if len(p)==10:
    print('The phone number is',p)
else:
    print("Your input doesn't contain a valid phone number!")
