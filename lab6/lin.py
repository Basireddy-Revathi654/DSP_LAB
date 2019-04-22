import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
def dft(x):
	y=[]
	j=cm.sqrt(-1)
	N=len(x)
	for k in range (0,N):
		sum=0
		for n in range (0,N)
			sum=sum+(x[n]*np.exp(-j*2*np.pi*n*k/N))
		np.append(y,sum)
	return y
x1=np.array(input("enter sequence one:")
y1=dft(x1)
x2=np.array(input(enter sequence two:"))
y2=dft(x2)
y=y1+y2
print y
x'1=2*x1
y'1=dft(x'1)
x'2=3*x2
y'2=dft(x'2)
y'=y'2+y'1
print y
	
