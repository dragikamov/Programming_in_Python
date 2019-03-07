#Problem 4

def to_meters(foot,inch):
    return ((foot*30.5)+(inch*2.54))

while True:
    x=int(input("Enter how many foots: "))
    y=int(input("Enter how many inches: "))
    if x==0 and y==0:
        break
    print("Converted to meters:",to_meters(x,y)/100,"\n")
