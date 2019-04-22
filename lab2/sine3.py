import matplotlib.pyplot as plt
import numpy as np
fs=300
f=9
x=np.arange(0,100,1)
y=np.sin(2*np.pi*f*x/fs)
plt.plot(x,y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()
