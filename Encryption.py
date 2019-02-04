import math
#data=input()
data='mynameisravgeet'
temp=[]
size=len(data)
r=math.floor(math.sqrt(size))
c=r+1

i=0
while i<size:
    temp.append(data[i:i+c])
    i+=c

code=''
n=0
while n!=c:
    for i in temp:
        code+=i[n]
    code+=' '
    n+=1
    print(code)
