'''
you are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

int size: the size of the rangoli
Returns

string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

#fixed Solution
import string
def print_rangoli(size):
    design=string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print("\n".join(L[::-1]+L[1:]))
   

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

----------------------------------------------------------------------------------------------------------------

import string
def print_rangoli(size):
    design=string.ascii_lowercase
    for i in reversed(range(n)):
        s="-".join(design[i:n])
        print((s[::-1]+s[1:]).center(3*n+2,"-")) # you can use 4*n-3 or 5*n-8
    for i in range(1,n):
        s="-".join(design[i:n]) # aplhabets prints one by one with adding - synbols
        print((s[::-1]+s[1:]).center(3*n+2,"-"))
   

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
