#散点图
import matplotlib.pyplot as plt
import numpy as np

N=200

plt.scatter(np.random.rand(N)*100,np.random.rand(N)*100,c='r',s=500,alpha=0.5)

plt.scatter(np.random.rand(N)*100,np.random.rand(N)*100,c='g',s=200,alpha=0.5)

plt.scatter(np.random.rand(N)*100,np.random.rand(N)*100,c='b',s=300,alpha=0.5)
# 三个数组，每组数据都包含了200个随机坐标的位置，C表示点的颜色，S表示点的大小，Alpha是透明度

plt.show()