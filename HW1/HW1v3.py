import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import itertools

"Del 1"
def read_coordinate_file(filename):
    """
    with open('HungaryCities.txt', mode='r') as file:
        A=[]
        r = 1
        for line in file:
            text = line.strip('{}\n')
            a,b = text.split(', ')
            a,b = float(a),float(b)
            x = b * (r * np.pi / 180)
            y = r * np.log(np.tan((np.pi / 4) + (np.pi * a / 360)))
            A.append([x,y])
    A = np.array(A)
    return A[:,0], A[:,1], A
    """

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
    coordinates = np.array(coordinates)
    return x1, y1, coordinates



"Del 2"
def plot_points(coordinates,indices,path):
    path = list(itertools.chain(*zip(path, path)))
    del path[1]
    del path[len(path) - 1]
    path = np.array(path)
    path = np.reshape(path, (int(len(path) / 2), 2))

    L_path = []
    for i in range(0, len(path)):
        cc_path = []
        for j in range(0, len(path[1, :])):
            cc_path.append(tuple(coordinates[path[i, j]]))
        L_path.append(cc_path)

    L = []
    for i in range(0, len(indices)):
        cc = []
        for j in range(0, len(indices[1, :])):
            cc.append(tuple(coordinates[indices[i, j]]))
        L.append(cc)

    lc = LineCollection(L, color=['k'], linewidth=0.5)
    lc1 = LineCollection(L_path, color=['r'])

    fig = plt.figure()
    ax = fig.gca()
    ax.add_collection(lc)
    ax.add_collection(lc1)
    ax.autoscale()
    plt.scatter(coordinates[:, 0], coordinates[:, 1], label='y-values')
    plt.xlabel('$x$')
    plt.legend()

"Del 3"
def construct_graph_connections(coordinates, radius):
    coordinates = np.array(coordinates)
    realdistance = []
    indices=[]
    for i in range(0, len(coordinates)-1):
        for j in range(i + 1, len(coordinates)):
            distance = np.linalg.norm(coordinates[i] - coordinates[j])
            if distance < radius:
                indices.append([i,j])
                realdistance.append(distance)
    realdistance = np.array(realdistance)
    indices = np.array(indices)
    return indices, realdistance




"Del 4"
def construct_graph(indices, realdistance, N):
    row = indices[:, 0]
    col = indices[:, 1]
    data = realdistance
    N = len(x)
    csr = csr_matrix((data, (row, col)), shape=(N, N)).toarray()
    return csr


"Del 6"
def find_shortest_paths(csr, start,end):
    csr1 = np.maximum(csr, csr.transpose())
    D, Pr = shortest_path(csr1, directed=False, method='FW', return_predecessors=True)
    path = [end] #list(range(0,len(csr))).remove(start)
    k = end #tuple(path)
    while Pr[start, k] != -9999:
        path.append(Pr[start, k])
        k = Pr[start, k]
    return D,Pr,path[::-1]


word = 1
if word == 1:
    mode = 'SampleCoordinates.txt'
    radius = 0.08
    start = 0
    end = 5
elif word == 2:
    mode = 'HungaryCities.txt'
    radius = 0.005
    start = 311
    end = 702
elif word == 3:
    mode = 'GermanyCities.txt'
    radius = 0.0025
    start = 1573
    end = 10584

x, y, coordinates = read_coordinate_file(mode)
N=len(x)
indices, realdistance = construct_graph_connections(coordinates, radius)
csr = construct_graph(indices, realdistance, N)
D,Pr,path = find_shortest_paths(csr, start,end)
plot_points(coordinates,indices,path)

#plot_points(coordinates,indices)
