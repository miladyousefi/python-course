while True:
    sum=0
    num = int(input("Enter a number  (0 for break) :"))
    if num == 0:
        break
    num_to_str=str(num)
    len_str=len(num_to_str)
    for i in range(0,len_str):
        #print(int(num_to_str[i]))
        digit=int(num_to_str[i])
        sum +=digit**len_str
    if sum==num:
        print("true")
    else:
        print("false")