# Problem 7

while True:
    n = int(input("Enter number of pens: "))
    if n < 0:
        break
    elif n<=50:
        print(n*45//100, "euros and", n*45%100, "cents")
    elif n<=100:
        print(n*38//100, "euros and", n*38%100, "cents")
    else:
        print(n*30//100, "euros and", n*30%100, "cents")