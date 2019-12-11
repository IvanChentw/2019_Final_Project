# plot image
def SaveImage(Z,TickLevel,PlotTitle,SaveLoc):
    fig,ax=plt.subplots()
    colourMap = plt.cm.jet
    plt.imshow(T,vmin=TickLevel.min(), vmax=TickLevel.max(),cmap=colourMap,interpolation='bicubic',origin='lower',
              extent=[X.min(), X.max(), Y.min(), Y.max()])
    plt.title(PlotTitle)
    plt.colorbar(ticks=TickLevel)
    plt.show()
    fig.savefig(SaveLoc)

    #For example:
    #SaveLoc='C:\\Users\\Ivan Chen\\final_project\\case6_1.png'

#Case6 A square heater with bounded triangular space.

import numpy as np
import matplotlib.pyplot as plt

#range of x and y:
x=30
y=30

#boundary temperature
up=25
down=25
left=25
right=25

#initialize condition in x-y for t:
X = np.arange(0, x, 1)
Y = np.arange(0, y, 1)
T = np.empty((x, y))
T.fill(25)

#set boundary temperature
def check(m,n):
    if x//2-1<=m<=x//2+1 and y//2-5<=n<=y//2-3:
        return True
    else:
        return False
    
for i in range(y):
    T[0][i]=up
    T[x-1][i]=down
    
for j in range(x):
    T[j][0]=left
    T[j][y-1]=right
    
for i in range(1, x-1):
    for j in range(1, y-1):
        if check(i,j): #middle=200,const temperature
            T[i][j]=100

# Set the tick of contour and colorbar
Lmin, Lmax = 20, 100
TickLevel = np.arange(Lmin,Lmax+1,20)
            
#print initial condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc01='C:\\Users\\Ivan Chen\\final_project\\case6_0.png'
'''
SaveImage(T,TickLevel,'Initial Temperature Distribution',SaveLoc01)

#Start repeating procedure 
def triangular(x,y): #boundary of triangle
    if y>0 and y-3**0.5*x<0 and y+3**0.5*x-30*(3**0.5)<0: 
        return True
    else:
        return False
    
repeat=5000
for iteration in range(0, repeat):
    for i in range(1, x-1, 1):
        for j in range(1, y-1, 1):
            if (not check(i,j)) and (triangular(i,j)):
                T[i,j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])
        
#print final condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc02='C:\\Users\\Ivan Chen\\final_project\\case6_1.png'
'''
SaveImage(T,TickLevel,'Final Temperature Distribution',SaveLoc02)
