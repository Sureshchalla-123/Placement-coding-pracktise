'''
 FizzBuzz: Write a program that prints the numbers from 1 to 100. For multiples of 3, 
 print "Fizz" instead of the number. For multiples of 5, print "Buzz" instead of the number. 
 For multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''

def FizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz",end=" ")
        elif i%3==0:
            print("Fizz",end=" ")
        elif i%5==0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")

if __name__=='__main__':
    n=int(input())
    FizzBuzz(n)

