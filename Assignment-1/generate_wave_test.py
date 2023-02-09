import matplotlib.pyplot as plt
import math
from scipy import signal


x = []
y = []
for i in range(256):
    x.append(i)
    
    a = round(80*math.sin(math.radians(2*math.pi*8*i))+100)
    b = round(70*math.cos(math.radians(2*math.pi*32*i))+100)
    c = round(30*signal.square(math.radians(2*math.pi*8*i))+100)

    y.append(c)
plt.plot(x, y)
plt.show()