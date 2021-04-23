def fibo_1(n):
    f_1=1
    f_2=1
    if n <1:
        return "Incorrect input"
    if n==1 or n== 2 :
        return 1
    for i in range(1,n):
        c=f_1+f_2
        f_1=f_2
        f_2=c
    return c
"""def fibo_2(m):
    if m==1 or m==2:
        return 1
    return fibo_2(m-1)+fibo_2(m-2)"""

n=int(input("enter m :"))
print(fibo_1(n))