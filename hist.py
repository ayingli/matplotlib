#直方图
import matplotlib.pyplot as plt
import numpy as np

data=[np.random.randint(0,n,n) for n in [3000,4000,5000]]
#生成包含三个数组的数组，第一个数组包含3000个随机数，范围为【0，3000），第二个数据包含4000个随机数，范围为【0，4000），第三个数组包含了5000个随机数，范围为【0，5000）
labels=['3K','4K','5K']
bins=[0,100,500,1000,2000,3000,4000,5000]
#bins数组指定直方图的边界，【0，100）会有一个数据点，【100，500）会有一个数据点，以此类推，一共有7个数据点

plt.hist(data,bins=bins,label=labels)
plt.legend()

plt.show()