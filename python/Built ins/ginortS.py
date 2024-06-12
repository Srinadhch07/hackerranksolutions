'''

You are given a string .
 contains alphanumeric characters only.
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
string=input()
odd=''
even=''
lower=''
upper=''
for i in string:
    if i.isupper():
        upper+=i
    elif i.islower():
        lower+=i
    elif i.isdigit():
        if int(i)%2==0:
            even+=i
        else:
            odd+=i
print("".join(sorted(lower))+"".join(sorted(upper))+''.join(sorted(odd))+"".join(sorted(even)))
