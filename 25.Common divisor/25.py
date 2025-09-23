import math

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

lcm = math.lcm(a,b)
hcf = math.gcd(a,b)
print("The LCM of the numbers is : ",lcm)
print("The greatest common divisor of the numbers is : ",hcf)

