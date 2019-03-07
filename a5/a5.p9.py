"""
JTSK-350111
problem 5.9.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def longest_word(lst):
    nr_word=0
    maxx=0
    max_word=0
    for words in lst:
        if (maxx<len(words)):
            maxx=len(words)
            max_word=nr_word
        nr_word+=1
    return lst[max_word]

string=input("Enter the string: ")
lst=string.split()
print("The longest word is:",longest_word(lst))
