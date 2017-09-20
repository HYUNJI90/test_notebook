import numpy as np
from math import log
import matplotlib.pyplot as plt

x=[] y=[]

def generateProfit (d):
    
    global s
    
    if d >= s:
        return 0.6*s
    else:
        return 0.6*d - 0.4*(s-d)

maxprofit = 0 
    
for s in range(20, 305):
    
    for i in range(1,1000):
        d = np.random.randint(10, high=200)
        profit = generateProfit(d)
        
        if profit > maxprofit:
            maxprofit = profit
            
x.append(s)

y.append(log(maxprofit))

plt.plot(x,y)

print("Max Profit:", maxprofit)