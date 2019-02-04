#Profile -> GeekRavD
#PYTHON PROGRAM TO GET THE PROBABILTY OF COIN TOSS
print('!!!High Alert, Its GeekRavD\'s script!!!')
import random
coin=['head','tail']
total=int(input('Enter the times you want to toss the coin : '))
hcount=0
tcount=0
n=0
while n<total:
    toss=random.choice(coin)
    if toss=='head':
        hcount=hcount+1
    else:
        tcount=tcount+1
    n=n+1
print('Head count :',hcount,'Probabilty :',hcount/total)
print('Tail count :',tcount,'Probabilty :',tcount/total)
a=input()
