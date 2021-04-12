def sum_n_1(m):
    my_sum = 0
    i=0
    while i < m:
        my_sum = my_sum + i
        i+=1
    return my_sum
def sum_of_x(x,k):
    sum_x=0
    for i in range(2,k+1):
        sum_x=x**k
    return sum_x

n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
total=x
div=-1
for i in range(2,n+1):
    total=total+div*(sum_of_x(x,i)/sum_n_1(i))
    div *=-1
print("The sum of series is",round(total,2))
