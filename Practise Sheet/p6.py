#Problem 6

def substitute_vowels(s,ch):
    r=""
    for n in s:
        if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
            r+=ch
        else:
            r+=n
    return r

s="This is a sentence"
print(s)
n=substitute_vowels(s, 'o')
print(n)
