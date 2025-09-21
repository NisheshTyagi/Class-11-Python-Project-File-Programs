size = int(input("Enter the size : "))

for i in range(65,65+size):
    for j in range((i-65)+1):
        print(chr(i),end=' ')
    print()
