import time
print('Hello User')
print('   Program to find whether a smaller alphabet or a larger alphabet takes more time to print.')
print ('   Choose a particular alphabet')
s=str(input("Type a small alphabet : "))
l=str(input("Type a large alphabet : "))
#for small
ss=time.clock()
print (s)
fs=time.clock()
ts=fs-ss
#for large
sl=time.clock()
print (l)
fl=time.clock()
tl=fl-sl
print ()
if ts>tl:
    print ('   Time taken to print',s,'is greater than',l)
    print ('      Time for',s,':',ts,'seconds and Time for',l,':',tl,'seconds')
else:
    print ('   Time taken to print',l,'is greater than',s)
    print ('      Time for',l,':',tl,'seconds and Time for',s,':',ts,'seconds')
print()
exit=input('Press enter to exit!!!')
