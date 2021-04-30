def jam(a,b):
    return a+b
def tafrig(a,b):
    return a-b
def zarb(a,b):
    return a*b
def taghsim(a,b):
    return a/b
def tavan(a,b):
    return a**b



while True:
    print("Enter first number :")
    first=int(input())
    print("Enter second number :")
    second=int(input())
    print("********************")
    print("1 - jam")
    print("2 - tafrig")
    print("3 - zarb")
    print("4 - taghsim")
    print("5 - tavan")
    print("0 - break")
    status =input()
    if status=='0':
        break
    if status=='1':
        hasel=jam(first,second)
    if status=='2':
        hasel=tafrig(first,second)
    if status=='3':
        hasel=zarb(first,second)
    if status=='4':
        hasel=taghsim(first,second)
    if status=='5':
        hasel=tavan(first,second)
    print(hasel)
    print("enter 0 for break !")
    status=input()
    if status=='0':
        break