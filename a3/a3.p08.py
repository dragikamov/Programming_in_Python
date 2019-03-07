"""
JTSK-350111
problem 3.8.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

x=int(input("Enter integers:\n"))
sum=x
n=1
while (x!=(-9) and n<10):
    x=int(input())
    if x!=(-9):
        sum+=x
        n+=1
average=sum/n
print("The average is:",average)
