import math

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

d = (b**2) - (4*a*c)
if d > 0:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("First root : ",r1)
    print("Second root : ",r2)
if d < 0:
    print("There are no real roots")
if d ==0:
    r = (-b)/(2*a)
    print("There is only one real root : ",r)
    

