'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
Language
Pypy 3
More
12345678910
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
for i in range(n//2):
    j=int((i*2)+1)
    print(('.|.'*j).center(m,"-"))
print(("WELCOME").center(m,'-'))
for i in reversed(range(n//2)):
    j=int((i*2)+1)
    print(('.|.'*j).center(m,'-'))
    
Line: 9 Col: 30

Test against custom input
Python
You have earned 10.00 points!
You are now 145 points away from the gold level for your python badge.
19%255/400
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5
Compiler Message
Success
Input (stdin)
7 21
Expected Output
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
for i in range(n//2):
    j=int((i*2)+1)
    print(('.|.'*j).center(m,"-"))
print(("WELCOME").center(m,'-'))
for i in reversed(range(n//2)):
    j=int((i*2)+1)
    print(('.|.'*j).center(m,'-'))
    
