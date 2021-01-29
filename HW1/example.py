

R = 1
import numpy as np
import re
#with open('SampleCoordinates.txt', mode='r') as file:
#    text = file.read()
#x = text.split(sep=' ,')
"""
with open('SampleCoordinates.txt', 'r') as file:
    for line in file:
         print(line, end=',')
"""
#resultt = [float(d) for d in re.findall('-?\d+\.?\d*', text)]
"""
x = []
y = []
for i in range(1, len(resultt), 2):
    x = x + [resultt[i]]
    y = y + [resultt[i-1]]
x1 = np.array(x)
y1 = np.array(y)

result = np.array(resultt)
result1 = result.reshape(len(result) // 2, 2)
b = result1[:, 1]
a = result1[:, 0]
x = b * (R * np.pi / 180)
y = R * np.log(np.tan((np.pi / 4) + (np.pi * a / 360)))
"""
a = 0.1 * np.arange(1., 25.).reshape(2, 3, 4)
