#Problem 2

f=open("squares.txt",'w')
for n in range(6):
    x=int(input())
    f.write(str(x)+str(" ")+str(x*x)+str("\n"))
f.close()
