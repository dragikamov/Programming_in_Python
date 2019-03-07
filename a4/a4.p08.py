"""
JTSK-350111
problem 4.8.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def count_vowels(s):
    vowels=0
    for n in s:
        if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
            vowels+=1
        elif n=='A' or n=='E' or n=='I' or n=='O' or n=='U':
            vowels+=1
    return vowels

while True:
    sentence=input("Enter a string: ")
    if sentence=='':
        break
    print("The number of vowels in this string is:",count_vowels(sentence))
