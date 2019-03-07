"""
JTSK-350111
problem 3.9.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def print_rectangle(n,m,c):
    for i in range(n):
        for j in range(m):
            print(c,end="")
        print("\n",end="")
                    
n=int(input("Enter an integer n:"))
m=int(input("Enter an integer m:"))
c=input("Enter a character c:")
print_rectangle(n,m,c)
