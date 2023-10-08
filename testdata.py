import types
import numpy as np

# linear dataset
data1 = types.SimpleNamespace()
data1.x = np.arange(0,20,0.5)
data1.y = np.sin(data1.x)+np.random.normal(size=len(data1.x))*0.1
data1.dy = 0.1

# histogram type dataset
data2 = types.SimpleNamespace()
data2.x = np.linspace(-1,5,100)
data2.y = np.random.poisson(lam= (1e4*np.exp(-data2.x))*(data2.x>0)+50) # exponential decay with shot noise

# 2d data 
data3 = types.SimpleNamespace()
data3.x = np.linspace(-3,3,20)
data3.y = np.linspace(0,10,30)
data3.z = np.outer(np.exp(-data3.x**2),np.sqrt(data3.y))