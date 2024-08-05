
def CetoFe(c):
    f=(c*9/5)+32
    return f
# end of function
c=eval(input("Enter celcius:"))
print(CetoFe(c))
'''

'''
def isPrime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
    return(flag)
# end of function
n=int(input("Enter number: "))
print(isPrime(n))

for i in range(100,1001):
    if isPrime(i):
        flag=True
        print(i)
        '''
'''
def DecToBin(n):
    Bin=" "
    while n>0:
        r=n%2
        n=n//2
        Bin=str(r)+Bin
    return int(Bin)
# end of function
n=int(input("Enter number:"))
print(DecToBin(n))


def BinToDec(n):
    Dec=0
    p=0
    while n>0:
        r=n%10
        n=n//10
        Dec=Dec+(r*2**p)
        p=p+1
    return Dec
# end of function
n=int(input("Enter number: "))
print(BinToDec(n))





