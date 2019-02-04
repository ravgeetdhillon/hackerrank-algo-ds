a=int(input('Enter a number : '))
if a==1:
    print ('1 is a neither prime nor composite number.')
else:
    for i in range(2,a):
        if a%i==0:
            if a%2==0:
                print ('Not a Prime number and even.')
            else:
                print ('Not a Prime number and odd.')
            break
    else:
        if a%2==0:
            print('A Prime Number and Even')
        else:
            print('A Prime Number and Odd')
            print(thanks)
