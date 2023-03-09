'''
 Palindrome: Write a program that checks whether a given string is a palindrome 
 (i.e., reads the same backward as forward).
'''

def isPalindrome(str):
    rev=stringReverse(str)
    if str == rev:
        return "Palindrome"
    else :
        return "Not a Plaindrome"

def stringReverse(str):
    l=len(str)
    revstr=""
    for i in range(l-1,-1,-1):
        revstr=revstr+str[i]
    return revstr

if __name__ == "__main__":
    str=input().strip()
    res=isPalindrome(str)
    print(res)