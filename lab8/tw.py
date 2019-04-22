import numpy as np
import matplotlib.pyplot as plt
m=32
n=np.arange(0,31)
x=(m-1)/2.0
y=np.abs(n-x)
z=y/(m-1)
z1=2*z
t=1-z1
plt.stem(t)
plt.show()
