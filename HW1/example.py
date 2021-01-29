import matplotlib.pyplot as plt

#R = 1
import numpy as np
import re
#with open('SampleCoordinates.txt', mode='r') as file:
#    text = file.read()
#x = text.split(sep=' ,')
"""
with open('SampleCoordinates.txt', 'r') as file:
    for line in file:
         print(line, end=',')
"""
#resultt = [float(d) for d in re.findall('-?\d+\.?\d*', text)]
"""
x = []
y = []
for i in range(1, len(resultt), 2):
    x = x + [resultt[i]]
    y = y + [resultt[i-1]]
x1 = np.array(x)
y1 = np.array(y)

result = np.array(resultt)
result1 = result.reshape(len(result) // 2, 2)
b = result1[:, 1]
a = result1[:, 0]
x = b * (R * np.pi / 180)
y = R * np.log(np.tan((np.pi / 4) + (np.pi * a / 360)))
"""
"""
plt.figure()
plt.plot([1, 2, 3, 4], [1, 2.5, 3.1, 4], label='Data 1')
plt.ylabel('Data 1 [m]')
plt.legend()

plt.twinx()

plt.scatter( [1, 2, 3, 4], [60, 48, 42, 30], label='Data 2' )
plt.ylabel('Data 2 [kg]')
plt.legend()

plt.xlabel('X')
plt.show()
"""
x = np.array([1,2,3])
x=x[None, :]
y = np.array([1,1,1])
y = y[None, :]
xy=np.concatenate((x, y), axis=0)
z=np.zeros([3,3])
for i in range(0,len(x[0,:])):
    for j in range(1,len(x[0,:])):
        z[i,j]=\

#[np.sqrt((x[0,i]-x[0,j])**2 + (y[0,i]-y[0,j])**2)]


z1 = np.sqrt((x[0,0]-x[0,1])**2 + (y[0,0]-y[0,1])**2)
z2 = np.sqrt((x[0,0]-x[0,2])**2 + (y[0,1]-y[0,2])**2)