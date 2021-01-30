import matplotlib.pyplot as plt

R = 3
import numpy as np
from scipy.sparse import csr_matrix
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
x = np.array([1,2,3,4])
#x=x[None, :]
y = np.array([1,1,1,2])
#y = y[None, :]
#xy=np.concatenate((x, y), axis=0)
"""
for i in range(0,len(xy[:,0])):
    for j in range(0,len(x[0])):
        z = np.sqrt((x[0, j] - x[0, j+1]) ** 2 + (y[0, j] - y[0, j+1]) ** 2)


z1 = np.sqrt((x[0,0]-x[0,1])**2 + (y[0,0]-y[0,1])**2)
z2 = np.sqrt((x[0,0]-x[0,2])**2 + (y[0,1]-y[0,2])**2)
"""
""""""
xdistance = np.array([])
ydistance = np.array([])
index=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        xdistance = np.append([xdistance],[x[i]-x[j]])
        ydistance = np.append([ydistance],[y[i]-y[j]])
        index = index + [[i,j]]

xdistance1 = xdistance**2
ydistance1 = ydistance**2
realdistance = np.sqrt(xdistance1+ydistance1)
vector=[]
for r in range(0,len(realdistance)):
    if realdistance[r] > R:
        realdistance[r] = 0
indices = np.array(index)





row = indices[:,0]
col = indices[:,1]
data = realdistance
N = len(x)
csr = csr_matrix((data, (row, col)), shape=(N, N)).toarray()
diagonal = np.diagonal(csr)
csrt = csr.transpose()
csr1 = csr - diagonal + csrt
linjer = np.nonzero(csr)
L = [[(x[0], y[0]),(x[1], y[1])] + [(x[0], y[0]),(x[1], y[1])] ]
L = []
for i in range(0,len(linjer[0])):
    L = L +[[(x[linjer[0][i]], y[linjer[0][i]]),(x[linjer[1][i]], y[linjer[1][i]])]]












