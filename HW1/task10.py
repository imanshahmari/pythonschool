from HW1v2 import *
import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from numpy import linalg as LA
from random import random
from scipy.sparse.csgraph import shortest_path
from scipy.spatial import cKDTree

plt.figure()
plt.scatter(coordinates[:,0], coordinates[:,1])
tree = cKDTree(coordinates)
indicesnew=[]

indicesnew = tree.query_pairs(0.08)
indicesnew = list(indicesnew)
indicesnew = np.array(indicesnew)
"""
for i in range(0,len(coordinates)):
    idx = tree.query_pairs(0.08)
    #idx= sorted(tree.query_ball_point(coordinates[i], 0.08))
    #print(pts[idx])
    indicesnew.append(idx)
    
"""
"""
L3 = [coordinates[i] for i in indices]

L3 = []
for i in range(0, len(indices)):
    cc = []
    for j in range(0, len(indices[1, :])):
        cc.append(tuple(coordinates[indices[i, j]]))
    L3.append(cc)
indicesnew2 = indicesnew.
for i1 in range(0,len(indicesnew))
"""






