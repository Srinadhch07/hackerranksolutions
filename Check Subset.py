'''
ou are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Constraints

Output Format

Output True or False for each test case on separate lines.

Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
Explanation

Test Case 01 Explanation

Set  = {1 2 3 5 6}
Set  = {9 8 5 6 3 2 1 4 7}
All the elements of set  are elements of set .
Hence, set  is a subset of set .

Language
Python 3
More
12345678910
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    input()
    a=set(map(int,input().split()))
    input()
    b=set(map(int,input().split()))
    if a.issubset(b):
        print(True)
    else:
        print(False)



Line: 10 Col: 20

Test against custom input
Python
You have earned 10.00 points!
53/115 challenges solved.
46%
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
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Expected Output
True
False
False

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    input()
    a=set(map(int,input().split()))
    input()
    b=set(map(int,input().split()))
    if a.issubset(b):
        print(True)
    else:
        print(False)
