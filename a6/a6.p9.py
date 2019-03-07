"""
JTSK-350111
problem 6.9.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def scalar(list_v,list_w,n):
    p=0
    for x in range(n):
        p+=(list_v[x]*list_w[x])
    return p

def smallest(list_a,n):
    p=list_a[0]
    for x in range(n):
        if list_a[x]<p:
            p=list_a[x]
    return p

def largest(list_a,n):
    p=list_a[0]
    for x in range(n):
        if list_a[x]>p:
            p=list_a[x]
    return p

n=int(input("Enter an integer n: "))
list_v=[]
list_w=[]
print("Enter the vector v:",)
for x in range(n):
    list_v.append(float(input()))
tuple(list_v)
print("Enter the vector w:")
for x in range(n):
    list_w.append(float(input()))
tuple(list_w)
print("The scalar product is:",scalar(list_v,list_w,n))
small_v=smallest(list_v,n)
small_w=smallest(list_w,n)
print("The smallest component of v is:",small_v,
      "and is on position:",list_v.index(small_v))
print("The smallest component of w is:",small_w,
      "and is on position:",list_w.index(small_w))
