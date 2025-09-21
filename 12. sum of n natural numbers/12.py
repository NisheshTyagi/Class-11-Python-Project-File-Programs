n = int(input("Enter the range : "))
for i in range(1,n+1):
    print(i,end = ',')
print()
if n%2 == 0:
    print((n+1) * n/2)
else:
    print(((n+1) * (n//2)) + ((n+1)/2))
