import matplotlib.pyplot as plt
import numpy as np

labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']  #指定标签

data=np.random.rand(7)*100    #其他数据的随机数值

plt.pie(data,labels=labels,autopct='%1.1f%%')    #autopct 表示数值的精度格式
plt.axis('equal')     #设置了坐标轴大小一致
plt.legend()    #指明要绘制的图例

plt.show()