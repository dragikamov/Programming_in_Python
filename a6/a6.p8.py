"""
JTSK-350111
problem 6.8.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

dict ={"merry":"god", "christmas":"jul",
       "and":"och", "happy":"gott",
       "new":"nytt", "year":"˚ar"}

def translate(list_en):
    x=""
    list_en=list_en.lower()
    y=list_en.split()
    for n in y:
        x+=dict[n]
        x+=" "
    return x

string=input("Enter your greeting: ")
print("Translated into Swedish:\n", translate(string),sep="")
