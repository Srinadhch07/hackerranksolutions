'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

'''
#Code Logic
def swap_case(string):
        newstring=''
        for a in string: 
            # converting to uppercase. 
            if (a.isupper()) == True: 

                newstring += (a.lower())
            elif(a.islower()) == True:
                newstring += (a.upper())
            elif (a.isspace())==True:
                newstring+=a
            elif (a.isdigit()) == True:
                newstring+=a
            else:
                newstring+=a
        return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#Smart Work

def swap_case(string):
        return string.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


