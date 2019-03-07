"""
JTSK-350111
problem 4.10.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

data="Python is a great programming language"

list_words=data.split()
for i in list_words:
    print(i)

upper=data.upper()
print("\n",upper,sep="")

print("\n",data.find("programming"),sep="")

print("\n",data.replace('g','G'),sep="")
