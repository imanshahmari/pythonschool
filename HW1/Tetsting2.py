import numpy as np
import time
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import itertools
from scipy.spatial import cKDTree

"Del 1"
def read_coordinate_file(mode):
    start_time_read = time.time()

    with open(mode, mode='r') as file:
        A=[]
        r = 1
        for line in file:
            text = line.strip('{}\n')
            a,b = text.split(',')
            a,b = float(a),float(b)
            x = b * (r * np.pi / 180)
            y = r * np.log(np.tan((np.pi / 4) + (np.pi * a / 360)))
            A.append([x,y])
    A = np.array(A)

    print("--- %s seconds read_coordinate_file---" % (time.time() - start_time_read))
    return A[:,0], A[:,1], A


"Del 2"
def plot_points(coordinates,indicesnew):
    start_time_plot = time.time()
    """
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
    """
    L = [coordinates[i] for i in indicesnew]
    """
    L = []
    for i in range(0, len(indices)):
        cc = []
        for j in range(0, len(indices[1, :])):
            cc.append(tuple(coordinates[indices[i, j]]))
        L.append(cc)
    """
    lc = LineCollection(L, color=['k'], linewidth=0.5)
    #lc1 = LineCollection(L_path, color=['r'])

    fig = plt.figure()
    ax = fig.gca()
    ax.add_collection(lc)
    #ax.add_collection(lc1)
    ax.autoscale()
    plt.scatter(coordinates[:, 0], coordinates[:, 1], label='y-values')
    plt.xlabel('$x$')
    plt.legend()

    print("--- %s seconds plot_points---" % (time.time() - start_time_plot))

"Del 3"
def construct_graph_connections(coordinates, radius):
    start_time_construct_graph_connections = time.time()

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

    print("--- %s seconds construct_graph_connections---" % (time.time() - start_time_construct_graph_connections))
    return indices, realdistance


"Del 4"
def construct_graph(indices, realdistance, N):
    start_time_construct_graph = time.time()

    row = indices[:, 0]
    col = indices[:, 1]
    data = realdistance
    N = len(x)
    csr = csr_matrix((data, (row, col)), shape=(N, N)).toarray()

    print("--- %s seconds construct_graph---" % (time.time() - start_time_construct_graph))
    return csr


"Del 6"
def find_shortest_paths(csr, start,end):
    start_time_shoretest_path = time.time()

    csr1 = np.maximum(csr, csr.transpose())
    D, Pr = shortest_path(csr1, directed=False, method='FW', return_predecessors=True)


    path = [end] #list(range(0,len(csr))).remove(start)
    k = end #tuple(path)
    while Pr[start, k] != -9999:
        path.append(Pr[start, k])
        k = Pr[start, k]

    print("--- %s seconds find_shortest_paths---" % (time.time() - start_time_shoretest_path))
    return D,Pr,path[::-1]


def construct_fast_graph_connections(coordinates, radius):
    start_time_fast_graph_connections = time.time()
    tree = cKDTree(coordinates)
    indicesnew = tree.query_pairs(radius)
    indicesnew = list(indicesnew)
    indicesnew = np.array(indicesnew)

    print("--- %s seconds construct_fast_graph_connections---" % (time.time() - start_time_fast_graph_connections))
    return indicesnew

word = 2
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
#indices, realdistance = construct_graph_connections(coordinates, radius)
#csr = construct_graph(indices, realdistance, N)
#D,Pr,path = find_shortest_paths(csr, start,end)
indicesnew = construct_fast_graph_connections(coordinates, radius)
plot_points(coordinates,indicesnew)

#plot_points(coordinates,indices)
