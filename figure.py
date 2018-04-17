#一次绘制多个图形，一个窗口显示多个图形
import matplotlib.pyplot as plt
import numpy as np

data=np.arange(100,201)
plt.subplot(2,1,1)
plt.plot(data)

data2=np.arange(200,301)
#plt.figure()  #一个figure就是一个图形窗口，matplotlib.pyplot会有一个默认的figure，也可以通过plt.figure()创建多个
plt.subplot(2,1,2)   #前两个参数指定了subplot数量，以矩阵的形式来分割当前图形，两个整数分别指定矩阵的行数和列数，第三个参数指定矩阵的索引
plt.plot(data2)

plt.show()