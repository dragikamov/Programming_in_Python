#Problem 5

while True:
    s=input("Enter password for checking: ")
    if(s==""):
        break
    n=0
    for let in s:
        if let.isdigit()==True:
            n+=1
    if (len(s)<8 or n<3):
        print("PASSWORD IS BAD")
    else:
        print("PASSWORD IS GOOD")
