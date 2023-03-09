'''
 Prime numbers: Write a program that determines whether a given number is prime 
 (i.e., only divisible by 1 and itself).d
'''
def isprime(n):
    
    flag=False
    if n==1:
        return False
    elif n>1:
        try:
            for i in range(2,n):
                if n%i==0:
                    return False
                else:
                    return True
        except:
            print("Error")
    else:
        pass


if __name__=="__main__":
    n=int(input())
    res=isprime(n)
    print(res)
