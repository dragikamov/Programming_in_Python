#Problem 3

n=int(input())
a='A'
for x in range(n):
    n=0
    while n<=x:
        print(chr(ord(a)+n),end="",sep="")
        n+=1
    print("\n",end="")
