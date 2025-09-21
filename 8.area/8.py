import math

print("Welcome to Area calculator")
print("1. Area of circle")
print("2. Area of Square")
print("3. Area of Rectangle")
usr = int(input("Enter your choice : "))

if usr == 1:
    r = float(input("Enter the radius of the circle : "))
    area = math.pi * r * r
    print("The area of the circle is ",area)
elif usr == 2:
    a = float(input("Enter the side length of the square : "))
    area = a * a
    print("The area of  the square is ",area)
elif usr == 3:
    l = float(input("Enter the length of the rectangle : "))
    b = float(input("Enter the breadth of the rectangle : "))
    area = l * b
    print("The area of the rectangle is ", area)
else:
    print("Invalid input")
