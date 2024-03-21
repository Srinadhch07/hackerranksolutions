'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
'''
if __name__ == '__main__':
    list1=[]
    list2=[]
    values=[]
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1=[name,score]
        list2.append(list1)
    
    for i in list2:
            values.append(i[1])
    values.sort()
    values=list(set(values))
    for i in list2:
        if i[1]==values[1]:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
    
       
        
