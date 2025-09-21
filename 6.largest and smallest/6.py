a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
nums = [a,b,c]

largest = 0
smallest = a
for i in nums:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("The smallest number is ",smallest)
print("The largest number is ",largest)
