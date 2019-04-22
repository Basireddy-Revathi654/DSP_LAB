import numpy as np
from matplotlib import pyplot as plt
f=20
fs=400
x=np.arange(0,500)
y=np.sin((2*np.pi*x*20)/400)
n1=np.random.rand(y.shape[0])
n=y+n1
ry=-y
rn1=np.random.rand(ry.shape[0])
rn=ry+rn1
h=[1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3]
s1=np.convolve(y,h)
s2=np.convolve(n,h)
s3=np.convolve(rn,h)
s4=np.convolve(n,rn)
s5=np.convolve(y,-y)
plt.subplot(8,1,1)
plt.plot(y)
plt.subplot(8,1,2)
plt.plot(n1)
plt.subplot(8,1,3)
plt.plot(n)
plt.subplot(8,1,4)
plt.plot(s1)
plt.subplot(8,1,5)
plt.plot(s2)
plt.subplot(8,1,6)
plt.plot(s3)
plt.subplot(8,1,7)
plt.plot(s4)
plt.subplot(8,1,8)
plt.plot(s5)
plt.show()
