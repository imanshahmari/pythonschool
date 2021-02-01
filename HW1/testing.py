import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from numpy import linalg as LA
from random import random
from scipy.sparse.csgraph import shortest_path
"""
Ny = 10
x = np.arange(8)

from random import random

lines = []
lines1 = []
for i in np.arange(Ny):
    line = []
    line1 = []
    for xj in x:
        y = random() * 3 + 2 * i
        y1 = random() * 9 + i
        line.append((xj, y))
        line1.append((xj,y1))
    lines.append(line)
    lines1.append(line1)

from matplotlib.collections import LineCollection

line_segments = LineCollection(lines, colors = 'b')
line_segments1 = LineCollection(lines1, colors ='k')
fig = plt.figure(figsize=(15, 8))
ax = fig.gca()
ax.add_collection(line_segments)
ax.add_collection(line_segments1)
ax.set_ylim((0, 2 * Ny + 3))
ax.set_xlim((0, np.amax(x)))
plt.show()
"""
with open('SampleCoordinates.txt', mode='r') as file:
    A=[]
    r = 1
    for line in file:
       text = line.strip('{}\n')
       a,b = text.split(', ')
       a,b = float(a),float(b)
       x = b * (r * np.pi / 180)
       y = r * np.log(np.tan((np.pi / 4) + (np.pi * a / 360)))
       A.append([x,y])
coordinates = np.array(A)


realdistance = []
indices=[]
for i in range(0, len(coordinates)-1):
    for j in range(i + 1, len(coordinates)):
        distance = np.linalg.norm(coordinates[i] - coordinates[j])
        if distance < 0.08:
            indices.append([i,j])
            realdistance.append(distance)
realdistance = np.array(realdistance)
indices = np.array(indices)