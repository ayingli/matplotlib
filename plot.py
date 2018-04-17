import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3],[3,6,9],'-r')    #plot函数的第一个数组是横轴的值，第二个数组是纵轴的值，第三个参数由两个字符构成，分别是线条的样式和颜色
plt.plot([1,2,3],[2,4,9],':g')

plt.show()