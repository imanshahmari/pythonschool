import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from numpy import linalg as LA

xc = np.array([[ 1 ,0], [ 8  ,9]])
svar1 = np.linalg.norm(xc[0]-xc[1])

svar2 = np.sqrt((1-8)**2 + (9)**2)