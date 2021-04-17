n=int(input("Enter n :"))
x=int(input("Enter x :"))
sum=x
k=1
pow_of_x=1
def sum_of_odd(n):
    sum_of_odd=0
    for i in range(0,n+1,2):
            sum_of_odd +=i   
    return sum_of_odd
def sum_of_even(n):
    sum_of_even=0
    for i in range(1,n+1,2):
        sum_of_even +=i
    return sum_of_even
for i in range(1, n + 1):
    if i%2 == 0:
        sum=sum+k*(x**pow_of_x/sum_of_odd(i))
    else:
        sum=sum+k*(x**pow_of_x/sum_of_even(i))
    pow_of_x=pow_of_x+i
    #print("x ^",k*pow_of_x)
    k*=-1
print(sum)