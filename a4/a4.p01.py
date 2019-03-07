"""
JTSK-350111
problem 4.1.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def leng(s):
    count=0
    for n in s:
        count+=1
    return count

sen=input("Enter the string: ")
print("The length of the string is:",leng(sen))
