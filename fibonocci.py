'''
Fibonacci sequence: Write a program that generates the first n numbers in the Fibonacci 
sequence (where each number is the sum of the two preceding ones).
'''
def fibonocci(n):
    
    #creationg the array
    arr=[0]*n
    arr[0]=0
    arr[1]=1
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]
    for i in range(n):
        print(arr[i],end=" ")

if __name__ == "__main__":
    n=int(input())
    fibonocci(n)