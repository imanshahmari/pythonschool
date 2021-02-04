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
path = list(itertools.chain(*zip(path, path)))

del path[1]
del path[len(path) - 1]
path = np.array(path)
path = np.reshape(path, (int(len(path) / 2), 2))

distancenew=[]
for i in path:
    coordinatesnew1 = coordinates[i][0]
    coordinatesnew2 = coordinates[i][1]
    distance = np.linalg.norm(coordinatesnew1-coordinatesnew2)
    distancenew.append(distance)
distancenew = np.array(distancenew)
Total_distance= sum(distancenew)

