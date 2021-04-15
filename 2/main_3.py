str=""
for row in range(0,7):
    for column in range(0,7):
        if(column==1 or (row)):
            str=str+"*\n"
print(str)
        