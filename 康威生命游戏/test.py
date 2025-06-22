import numpy as np
import matplotlib.pyplot as plt
# x = np.array([[0,0,1],[1,1,0],[0,1,0]])
# plt.imshow(x)
# plt.show()
x = np.array([[1,1,1],
             [1,0,0],
             [0,1,0]])
g = np.zeros(5*5).reshape(5,5)
g[1:4,1:4] = x
plt.imshow(g)
plt.show()