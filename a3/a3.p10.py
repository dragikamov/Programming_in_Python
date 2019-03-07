"""
JTSK-350111
problem 3.10.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def print_frame(n,m,c):
    for i in range(n):
        for j in range(m):
            if i==0 or i==n-1:
                print(c,end="")
            else:
                if j==0 or j==m-1:
                    print(c,end="")
                else:
                    print(" ",end="")
        print("\n",end="")
                    
n=int(input("Enter an integer n:"))
m=int(input("Enter an integer m:"))
c=input("Enter a character c:")
print_frame(n,m,c)
