size = int(input("Enter the size of the patterns : "))


print('Pattern 1\n\n')
for i in range(size):
    for j in range(i):
        print('*',end='')
    print()
print('\n\n')
print('Pattern 2\n\n')
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print()
print('\n\n')
print('Pattern 3\n\n')

for i in range(size,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
        
