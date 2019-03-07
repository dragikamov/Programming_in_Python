#Problem 7

while True:
    pen=int(input("Enter number of pens: "))
    if pen<0:
        break
    elif pen<=50:
        price=pen*45
    elif pen<=100:
        price=pen*38
    else:
        price=pen*38
    print("The price of the pens is:",price//100,"euros and",price%100,"cents.")
