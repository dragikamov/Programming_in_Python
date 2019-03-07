"""
JTSK-350111
problem 5.2.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

f=open("numbers.txt",'r')
summ=0
for line in f:
    if line=="\n":
        continue
    num=int(line)
    summ+=num
f.close()
print("The sum of the numbers is:",summ)
