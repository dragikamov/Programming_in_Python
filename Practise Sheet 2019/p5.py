# Problem 5

def count_num(s):
    n = 0
    for i in s:
        if 48 <= ord(i) <= 57:
            n+=1
    return n

while True:
    s = input("Enter the password: ")
    if s =="":
        break
    elif len(s)<8 or count_num(s)<3:
        print("PASSWORD IS BAD")
    else:
        print("PASSWORD IS GOOD")