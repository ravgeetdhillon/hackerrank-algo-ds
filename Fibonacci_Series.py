def fb(n):
    if n==0 or n==1:
        return 1
    else:
        return fb(n-1)+fb(n-2)
print(fb(5))
a=input()
