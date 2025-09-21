n = int(input("Enter the range : "))
if n%2 == 0:
    natural = int(((n+1) * n/2))
else:
    natural = int((n+1) * (n//2)) + ((n+1)/2)
sum = 0
for i in range(1,n+1):
    for j in range(1,i):
        sum+=j

print(sum)
