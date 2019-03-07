# Problem 2

lst = []
for i in range(6):
    lst.append(int(input()))
f = open("squares.txt",'w')
for i in range(5,-1,-1):
    f.write(str(lst[i]) + " " + str(lst[i]**2) + "\n")
f.close()
