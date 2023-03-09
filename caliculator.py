'''
Calculator: Write a program that performs basic arithmetic operations (addition, subtraction, multiplication, 
and division) on two numbers inputted by the user.
'''

class Caliculator():

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return a+b
    def sub(self):
        return a-b
    def mul(self):
        return a*b
    def div(self):
        return a/b


if __name__=='__main__':
    a,b=map(int,input().split())
    obj=Caliculator(a,b)
    while(True):
        print("Enter 1(add), 2(sub), 3(mul), 4(div), 5(exit) :",end=" ")
        opt=int(input())
        if opt==1:
            print(obj.add())
        elif opt==2:
            print(obj.sub())
        elif opt==3:
            print(obj.mul())
        elif opt==4:
            print(obj.div())
        elif opt==5:
            exit()
        else:
            print("Wrong option !")
        
