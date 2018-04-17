#直方图
import matplotlib.pyplot as plt
import numpy as np

N=7

x=np.arange(N)

data=np.random.randint(low=0,high=100,size=N)    #生成7个随机数
colors=np.random.rand(N*3).reshape(N,-1)   #生成随机颜色，先生成21（N*3）个随机数，然后将他们装成七行，每行三个数，对应颜色的三个组成部分
labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

plt.title('Weekday Data')
plt.bar(x,data,alpha=0.8,color=colors,tick_label=labels)
plt.show()