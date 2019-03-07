# Problem 8

def find_min(lst):
    m = lst[0]
    for i in range(1,len(lst)):
        if lst[i] < m:
            m = lst[i]
    return m

lst = []
n = int(input("Enter the number of elements in the list: "))
print("Now enter the list:")

for i in range(n):
    lst.append(int(input()))

print("\nThe minimum is",find_min(lst))