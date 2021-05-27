import pandas as pd
import matplotlib.pyplot as plt

iris=pd.read_csv('data/iris.csv')
data=pd.DataFrame(iris)
plt.plot(data['sepal_width'],data['sepal_length'],'o')
#ax=plt.axes()
#ax.set(facecolor="green")
plt.xlabel('sepal_width')
plt.ylabel('sepal_length')
plt.show()