# Problem 3

n = int(input())
for i in range(1,n+1):
    c = 'A'
    for j in range(i):
        print(chr(ord(c)+j),end="")
    print()