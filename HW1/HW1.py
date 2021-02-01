import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
"Del 1"
def read_coordinate_file(filename):
    r = 1
    with open(filename, mode='r') as file:
        text = file.read()
    resultt = [float(d) for d in re.findall('-?\d+\.?\d*', text)]
    result = np.array(resultt)
    result1 = result.reshape(len(result) // 2, 2)
    b = result1[:, 1]
    a = result1[:, 0]
    x1 = b * (r * np.pi / 180)
    y1 = r * np.log(np.tan((np.pi / 4) + (np.pi * a / 360)))
    coordinates = []
    for i in range(0,len(x1)):
        coordinates = coordinates + [[x1[i],y1[i]]]
    return x1, y1, coordinates

x, y, coordinates = read_coordinate_file('SampleCoordinates.txt')


"Del 2"
def plot_points(x2,y2,csr):
    linjer = np.nonzero(csr)
    L = []
    for i in range(0, len(linjer[0])):
        L = L + [[(x[linjer[0][i]], y[linjer[0][i]]), (x[linjer[1][i]], y[linjer[1][i]])]]
    lines = L
    lc = LineCollection(lines, color=['k'],linewidth=0.5)
    fig = plt.figure()
    ax = fig.gca()
    ax.add_collection(lc)
    ax.autoscale()
    plt.scatter(x2, y2, label='y-values')
    plt.xlabel('$x$')
    plt.legend()
    return plt.show()

"Del 3"
def construct_graph_connections(x3,y3, radius):
    xdistance = np.array([])
    ydistance = np.array([])
    index = []
    for i in range(0, len(x3)):
        for j in range(i + 1, len(x3)):
            dx = x3[i] - x3[j]
            dy = y3[i] - x3[j]
            xdistance = np.append([xdistance], [x3[i] - x3[j]])
            ydistance = np.append([ydistance], [y3[i] - y3[j]])
            index = index + [[i, j]]

    xdistance1 = xdistance ** 2
    ydistance1 = ydistance ** 2
    realdistance = np.sqrt(xdistance1 + ydistance1)
    for r in range(0, len(realdistance)):
        if realdistance[r] > radius:
            realdistance[r] = 0
    indices = np.array(index)
    return indices, realdistance

"Del 4"
def construct_graph(indices, realdistance, N):
    row = indices[:, 0]
    col = indices[:, 1]
    data = realdistance
    N = len(x)
    csr = csr_matrix((data, (row, col)), shape=(N, N)).toarray()
    return csr



