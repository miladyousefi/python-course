sum_of_nums=1
n=int(input("Enter value for n :"))
x=int(input("Enter value for x :"))
for i in range(1,n+1):
    sum_of_nums=sum_of_nums + x**i/i
print(sum_of_nums)