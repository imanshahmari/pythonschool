"""
SampleCoordinates.txt
GermanyCities.txt

"""
"Indata"

R = 1
import numpy as np
import re
with open('SampleCoordinates.txt', mode='r') as file:
    text = file.read()
resultt = [float(d) for d in re.findall('-?\d+\.?\d*',text)]
#result = np.array(resultt)
x = []
y = []
for i in range(1, len(resultt), 2):
    x = x + [resultt[i]]
    y = y + [resultt[i-1]]
x1 = np.array(x)
y1 = np.array(y)
x1 = x * (R * np.pi / 180)
y1 = R * np.ln(np.tan((np.pi/4)+(np.pi*y/360)))
