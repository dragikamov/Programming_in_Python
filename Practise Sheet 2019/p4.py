# Problem 4

def to_meters(foot, inch):
    meters = (foot * 30.5 + inch * 2.54)/100
    return meters

while True:
    foot = int(input("Enter foot: "))
    inch = int(input("Enter inch: "))
    if foot == 0 and inch == 0:
        break
    print("Converted to meters that is:",to_meters(foot,inch))