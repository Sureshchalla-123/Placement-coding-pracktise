'''
Find the largest number: Write a program that takes an array of integers as input and outputs the 
largest number in that array.
'''
import random

def largestOfArray(arr):
    l=len(arr)
    large=0
    for i in range(l):
        if arr[i]>large:
            large=arr[i]
    return large

def largestOfArray1(arr):
    l=len(arr)
    arr.sort()
    return arr[l-1]

if __name__=='__main__':
    arr=list(map(int,input().split()))
    res=largestOfArray1(arr)
    print(res)