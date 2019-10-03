# Include the two lines below to open a window
#import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as m3d
import numpy as np
#matplotlib.interactive(True)
ax = m3d.Axes3D(plt.figure())

X = np.random.uniform(0, 1, [100,3])

ax.scatter3D(*X.T)
ax.set_aspect('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 10)
plt.show()

#%%
#import pptk

#pptk.viewer(X)
