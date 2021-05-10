'''matplotlib intro and start...'''
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.scatter([9, 8, 7], [6, 5, 4], label='first', linewidth=4)
plt.plot([1, 2, 3], [4, 5, 6], label='second', linewidth=4)
# plt.arrow([1,2,3],[4,5,6],label='third',linewidth=4)
plt.title('random data')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.legend()
plt.show()
