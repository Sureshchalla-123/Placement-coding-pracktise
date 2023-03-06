class Main():
    def addTwo(self,a,b):
        return a+b
    
if __name__=='__main__':
    a,b=map(int,input().strip().split(" "))
    obj=Main()
    res=obj.addTwo(a,b)
    print(res)