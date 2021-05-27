import random 

def my_random(start, end,count):
    my_list = []
    for i in range(0, count):
        my_rand_int=random.randint(start, end)
        my_list.append(my_rand_int)
    return my_list
my_list=my_random(10,200,10)
print(my_list)
print()

m=random.choices(my_list,weights=[3,1,1,1,2,3,2,1,4,2],k=40)
n=random.sample(m,k=5)
print(m)
print()
print(n)
