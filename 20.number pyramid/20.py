size = int(input("Enter the size : "))
n = 0
for i in range(1,size+1):
    for j in range(i):
         n+=1
         print(n,end=' ')
    print()
