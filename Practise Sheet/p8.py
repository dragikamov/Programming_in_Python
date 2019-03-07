#Problem 8

def ssort(lis,n):
    for x in range(n-1):
        for y in range(x+1,n):
            a=lis[x]
            b=lis[y]
            if (a>b):
                dummy=lis[x]
                lis[x]=lis[y]
                lis[y]=dummy

n=int(input("Enter how big the list is: "))
lis=[]
print("Enter the list:")
for x in range(n):
    lis.append(int(input()))

ssort(lis,n)
print("The smallest number of the list is:",lis[0])
