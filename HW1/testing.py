import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from numpy import linalg as LA
from random import random
from scipy.sparse.csgraph import shortest_path
csr1 = np.maximum(csr, csr.transpose())
D, Pr = D, Pr = shortest_path(csr1, directed=False, method='FW', return_predecessors=True)
