
class Main():
    def pattern1(self,h):
        character = '* '
        for i in range(1,h+1):
            print(character*i)
  

if __name__=='__main__':
    h=int(input("Enter height "))
    obj=Main()
    obj.pattern1(h)
