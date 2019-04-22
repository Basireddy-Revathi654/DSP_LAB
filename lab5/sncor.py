import numpy as np
from matplotlib import pyplot as plt
f=20
fs=400
x=np.arange(0,100,0.1)
y=np.sin((2*np.pi*x*20)/400)
n1=np.random.rand(y.shape[0])
n=y+n1
h=[1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3]
s=np.convolve(n,h)
plt.subplot(4,1,1)
plt.plot(x,y)
plt.subplot(4,1,2)
plt.plot(n1)
plt.subplot(4,1,3)
plt.plot(n)
plt.subplot(4,1,4)
plt.plot(s)
plt.show()