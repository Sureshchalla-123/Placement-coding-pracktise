class Main():
    def pyramid(self,n):
        """
        Prints a full pyramid of asterisks (*) with n rows.
        """
        for i in range(n):
            print(' '*(n-i-1) + '*'*(2*i+1) + ' '*(n-i-1))


       
if __name__=='__main__':
    h=int(input("Enter height"))
    obj=Main()
    obj.pyramid(h)
