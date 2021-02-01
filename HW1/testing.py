import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from numpy import linalg as LA
from random import random
from scipy.sparse.csgraph import shortest_path

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