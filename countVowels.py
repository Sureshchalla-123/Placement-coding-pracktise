'''
Count vowels: Write a program that takes a string as input and outputs the number of vowels in that 
string. For this problem, we consider the vowels to be "a", "e", "i", "o", and "u".
'''
def coutnVowels(str):
    l=len(str)
    coutnt=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in range(l):
        if str[i] in vowels:
            coutnt+=1
    return coutnt

        

if __name__=='__main__':
    string=input()
    res=coutnVowels(string)
    print(res)
