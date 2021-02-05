import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import itertools
from scipy.spatial import cKDTree

"Del 1"
def read_coordinate_file(mode):
    start_time_read = time.time()

    """Description of the Function
        Reads file into list. Cleans the data and then converts it to x and y coordinates 
        Parameters: 
        File 

        Returns:
        List of coordinates x,y and xy together
        
        pydoc -w read_coordinate_file

    """

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
def plot_points(coordinates,indices,path):
    start_time_plot = time.time()

    """ Description of the Function
        Makes scatter plot,Line collection, shortestpath and all connections between cities  
        Parameters: 
        coordinates,indices,path

        Returns:
        plots shortest path in red, Connections and coordinates(scatter) 
    
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

    L = [coordinates[i] for i in indices]


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

    print("--- %s seconds plot_points---" % (time.time() - start_time_plot))

"Del 3"
def construct_graph_connections(coordinates, radius):
    start_time_construct_graph_connections = time.time()

    """ Description of the Function
        constructs graph conncetions between the points in the scatter plot but slow  
        Parameters: 
        coordinates, radius

        Returns:
        The indices and distances between all the points 

    """
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

    """ Description of the Function
        Calculates the csr matrix 
        Parameters: 
        indices, realdistance, N (length of x axis) 

        Returns:
        csr matrix  

    """

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

    """ Description of the Function
        finds the shortest path from start to all other cities  
        Parameters: 
        csr, start city , end city 

        Returns:
        csr matrix  

    """


    D, Pr = shortest_path(csr,indices=start, directed=False, return_predecessors=True)
    path = [end] #list(range(0,len(csr))).remove(start)
    k = end #tuple(path)
    while Pr[k] != -9999:
        path.append(Pr[k])
        k = Pr[k]

    print("--- %s seconds find_shortest_paths---" % (time.time() - start_time_shoretest_path))
    return D,Pr,path[::-1]

def construct_fast_graph_connections(coordinates, radius):
    start_time_fast_graph_connections = time.time()

    """ Description of the Function
        construct_fast_graph_connections  this one is a better version of the previous one 
        Parameters: 
        coordinates, radius 

        Returns:
        indices and distances   

    """

    tree = cKDTree(coordinates)
    indicesnew = tree.query_pairs(radius)
    indicesnew = list(indicesnew)
    indicesnew = np.array(indicesnew)

    distancenew=[]
    for i in indicesnew:
        coordinatesnew1 = coordinates[i][0]
        coordinatesnew2 = coordinates[i][1]
        distance = np.linalg.norm(coordinatesnew1-coordinatesnew2)
        distancenew.append(distance)
    distancenew = np.array(distancenew)
    print("--- %s seconds construct_fast_graph_connections---" % (time.time() - start_time_fast_graph_connections))
    return indicesnew, distancenew


"Set word to 1 to run with Sample coordinates, 2 for run Hungary and 3 for run Germany "
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


" Calling function in the order they should be called "

x, y, coordinates = read_coordinate_file(mode)
N=len(x)
#indices, realdistance = construct_graph_connections(coordinates, radius)
indices, realdistance = construct_fast_graph_connections(coordinates, radius)
csr = construct_graph(indices, realdistance, N)
D,Pr,path = find_shortest_paths(csr, start,end)
plot_points(coordinates,indices,path)




" Calculating Total distance for the shortest path "
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
print("--- %s Total distance---" % (Total_distance))


