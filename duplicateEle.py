'''
Find duplicates: Write a program that takes an array of integers as input and outputs any 
duplicate elements in that array.
'''
def duplicateEle(arr):
    l=len(arr)
    duplicate=[]
    count=0
    ele=0
    for i in range(l):
        if arr[i] in duplicate:
            continue
        ele=arr[i]
        for j in range(l):
            if arr[j]==ele:
                count+=1
        if count>1:
            duplicate.append(ele)
        count=0
    return duplicate

if __name__=='__main__':
    arr=list(map(int,input().split()))
    res=duplicateEle(arr)
    print(res)