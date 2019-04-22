import matplotlib.pyplot as plt
import numpy as np
Fs=100
sample=100
x=np.arange(sample)
k=-100
new=0
j=input('enter the value j=')
for f in range (-100,j):
	new=new+np.sin(2*np.pi*f*x/Fs)
plt.plot(x,new)
plt.show()

