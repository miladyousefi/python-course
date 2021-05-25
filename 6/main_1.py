import matplotlib.pyplot as plt
import random
my_list_x=[]
my_list_y=[]
for i in range(0,1000):
    z=random.randint(10,100)
    my_list_y.append(z)
for i in range(0,1000):
    my_list_x.append(i)

plt.plot(my_list_x,my_list_y,'rs')
plt.show()
