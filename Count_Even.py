a=str(input('Enter a number to know the number of even number it contains : ))
count=0
for char in a:
    if int(char)%2==0:
        count=count+1
print(count)
