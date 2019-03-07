"""
JTSK-350111
problem 5.3.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

name=input("Enter the name of the file: ")
nline=1
f=open(name,'r')
for line in f:
    nwords=0
    if line!="\n":
        words=line.split()
        for word in words:
            nwords+=1
        print("In line",nline,"there are",nwords,"words.")
    else:
        print("Line",nline,"is empty.")
    nline+=1
f.close()
