n = int(input("Enter the range : "))
a=0
b=0
for i in range(1,n+1):
    for j in range(1,i+1):
        a+=j
    b+=a
    a=0
print(b)
