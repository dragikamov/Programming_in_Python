"""
JTSK-350111
problem 5.1.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

f1=open("input.txt",'r')
f2=open("output.txt",'w')
for line in f1:
    let=line.split()
    for elem in let:
        f2.write(str(ord(elem))+" ")
f1.close()
f2.close()
