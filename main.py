from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import config as cfg

#initial
fig = plt.figure()
ax = Axes3D(fig)
X=np.arange(-5,5.5,0.5)
Z= np.array([0]*21)

#function:y=f(x)
Y1=-X**2-1
Y2=np.array([2]*21)

#create two curve
curve1=cfg.curve(X,Y1,Z)
curve2=cfg.curve(X,Y2,Z)

#build the third curve
curve3=cfg.intersection(curve1,curve2)

#draw three curve
ax.plot(curve1.X,curve1.Y,curve1.Z)
ax.plot(curve2.X,curve2.Y,curve2.Z)
ax.plot(curve3.X,curve3.Y,curve3.Z)

#draw the surface
surface_X,surface_Z=np.meshgrid(curve3.X,curve3.Z)
surface_Y,surface_Z=np.meshgrid(curve3.Y,curve3.Z)
cfg.extend(surface_Z,curve3)
ax.plot_surface(surface_X, surface_Y, surface_Z, rstride=1, cstride=1,cmap='rainbow')
plt.show()

