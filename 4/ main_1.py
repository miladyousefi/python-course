n=int(input("Enter n :"))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")