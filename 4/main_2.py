def fact(n):
    total=1
    for i in range(1,n+1):
        total=total*i
    return total
sum_1=0
n= int(input('Enter n :'))
for k in range(1,n+1):
    sum_1 = sum_1 + k/fact(k)
print("Sum of the Series 1/1! + 2/2! + 3/3! +... + n/n! , n=",n)
print(sum_1)
print("-------------*******---------------")
sum_2=0
m=int(input('Enter m :'))
for j in range(1,m+1):
    sum_2=sum_2 + fact(j)
print("sum of 1!+2!+3!+ . . . + m! , m=",m)
print(sum_2)