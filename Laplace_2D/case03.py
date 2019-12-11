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

#Case3 A circle heater with bounded circle space.

import numpy as np
import matplotlib.pyplot as plt

#range of x and y:
x=50 
y=50
R=(y-1)/2

#check whether between center<(x,y,z)<R
def circle_with_center(x,y,center): 
    if (x-R)**2+(y-R)**2<R**2 and (x-R)**2+(y-R)**2>center**2:
        return True
    else:
        return False

#boundary temperature
inside=200
outside=20

#initialize condition in x-y for t:
X = np.arange(0, x, 1)
Y = np.arange(0, y, 1)
T = np.empty((x, y))
T.fill(outside)

#set boudary temperature
if (y-1)%2==0:
    T[(z-1)//2][(z-1)//2][(z-1)//2]=inside
for i in range(0,x,1):
    for j in range(0,y,1):
        if circle_with_center(i,j,0):
            T[i][j]=inside
            
# Set the tick of contour and colorbar
TickLevel = np.arange(20,201,20)

#print initial condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc01='C:\\Users\\Ivan Chen\\final_project\\case3_0.png'
'''

SaveImage(T,TickLevel,'Initial Temperature Distribution',SaveLoc01)


#Start repeating procedure 
repeat=5000
for iteration in range(0, repeat):
    for i in range(1,x-1,1):
        for j in range(1,y-1,1):
            if circle_with_center(i,j,1):
                T[i,j]=(1/4)*(T[i+1][j]+T[i-1][j]+T[i][j+1]+T[i][j-1])
            
#print final condition temperature 
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc02='C:\\Users\\Ivan Chen\\final_project\\case3_1.png'
'''
SaveImage(T,TickLevel,'Final Temperature Distribution',SaveLoc02)
