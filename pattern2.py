class Main():
    def pyramid(self,h):
        character="* "
        for i in range(1,h+1):
            for j in range(h,i,-1):
                print(" ",end=" ")
            print(character*i)


if __name__=='__main__':
    h=int(input("Enter height"))
    obj=Main()
    obj.pyramid(h)
