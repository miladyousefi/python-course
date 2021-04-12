# 1 + x/1 + x^2/2 + x^3/3 + .. .+ x^n/n
 
def SUM(x, n):
    total = 1
    for i in range(1, n + 1):
        total = total + ((x**i)/i)
    return total
 
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
s = SUM(x, n)
print(round(s, 2))