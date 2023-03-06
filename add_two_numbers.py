class Main:

    def addTwoNum(self,A,B):

        return A+B

    def subTwoNum(self,A,B):
        return A-B

    if __name__=='__main__':
        obj = Main()
        a=int(input())
        b=int(input())
        res=obj.addTwoNum(a,b)
        print(res)