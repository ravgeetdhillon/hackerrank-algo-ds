a=int(input('Factor of : '))
for i in range(2,a+1):
    if a%i==0:
        print('Factor of',a,':',i)
        break
exit=input('Press enter to exit')
                   
