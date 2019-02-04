import math
def imag(a,b):
    print (complex(a,b))
    v=math.sqrt((a**2)+(b**2))
    return v
a=int(input('Input real part : '))
b=int(input('Input complex part : '))
print(imag(a,b))
