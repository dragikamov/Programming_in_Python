"""
JTSK-350111
problem 5.4.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

name=input("Enter the name of the file: ")
f=open(name,'r')
copy=open("copy.txt",'w')
for line in f:
    copy.write(line)
f.close()
copy.close()
