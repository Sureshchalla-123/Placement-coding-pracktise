def revstr(str):
    l=len(str)
    for i in range(l-1,-1,-1):
        print(str[i],end="")

if __name__ == '__main__':
    name=input()
    revstr(name)
    
