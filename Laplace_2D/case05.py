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

#Case5 Two sides with linearly decreasing temperature bounded by square space.
import numpy as np
import matplotlib.pyplot as plt

#range of x and y:
x=20
y=20

#boundary temperature
up=200
down=25
left=25
right=200
delta=(right-100)/x

#initialize condition in x-y for t:
X = np.arange(0, x, 1)
Y = np.arange(0, y, 1)
T = np.empty((x, y))
T.fill(25)

#set boudary temperature
for i in range(y):
    T[0][i]=up-(y-i)*delta
    T[x-1][i]=down
    
for j in range(x):
    T[j][0]=left
    T[j][y-1]=right-j*delta
    
T[0][0]=65
T[0][y-1]=195
T[x-1][0]=25
T[x-1][y-1]=67.5

# Set the tick of contour and colorbar
TickLevel = np.arange(20,201,20)

#print initial condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc01='C:\\Users\\Ivan Chen\\final_project\\case5_0.png'
'''
SaveImage(T,TickLevel,'Initial Temperature Distribution',SaveLoc01)

#Start repeating procedure 
repeat=5000
for iteration in range(0, repeat):
    for i in range(1, x-1, 1):
        for j in range(1, y-1, 1):
                T[i,j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])
        
#print final condition temperature        
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc02='C:\\Users\\Ivan Chen\\final_project\\case5_1.png'
'''
SaveImage(T,TickLevel,'Final Temperature Distribution',SaveLoc02)
