# Problem 6

vowels = ['a','e','i','o','u','A','E','I','O','U']

def substitute_vowels(st, ch):
    s = ""
    for i in st:
        if i in vowels:
            s += ch
        else:
            s += i
    return s

s = "This is a sentence"
print(s)
n = substitute_vowels(s, 'o')
print(n)