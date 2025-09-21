size = int(input("Enter the size : "))
size += 1
for i in range(size,0,-1):
    for j in range(size - (size - i + 1)):
        print(' ',end='')
    for j in range((size - (size-i)),size):
        print(j,end='')
    print()
