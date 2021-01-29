import numpy as np
import re
import matplotlib.pyplot as plt

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
    x1 = x1[None, :]
    y1 = y1[None, :]
    return x1, y1

x, y = read_coordinate_file('SampleCoordinates.txt')

def plot_points(x2,y2):
    plt.scatter(x2, y2, label='y-values')
    plt.xlabel('$x$')
    plt.legend()
    plt.autoscale()
    return plt.show()

plot_points(x,y)
"""
def construct_graph_connections(x3,y3, radius):
    import numpy as np
    for i in range(0, len(x)):
        """


