principal = int(input("Enter your principal amount : "))
rate = float(input("Enter your rate : "))
time = float(input("Enter your time in years : "))
si = (principal * time* rate)/100
print('The simple interest is ',si)
print('The total amount is ',principal + si)
