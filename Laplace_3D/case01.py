# plot image
def SaveImage(Z,TickLevel,PlotTitle,SaveLoc):
    fig,ax=plt.subplots()
    colourMap = plt.cm.jet
    plt.imshow(Z,vmin=TickLevel.min(), vmax=TickLevel.max(),cmap=colourMap,interpolation='bicubic',origin='lower',
              extent=[X.min(), X.max(), Y.min(), Y.max()])
    plt.title(PlotTitle)
    plt.colorbar(ticks=TickLevel)
    plt.show()
    fig.savefig(SaveLoc)

#Case1 A two-sided square cubic heater. 
import matplotlib.pyplot as plt
import numpy as np

#range of x and y and z:
x=30
y=30
z=30

#boundary temperature for six sides
up=25
down=25
left=200
right=200
front=25
back=25

#initialize condition in x-y for t:
X = np.arange(0, x, 1)
Y = np.arange(0, y, 1)
Z = np.arange(0 ,z, 1)
T = np.empty((x,y,z))
T.fill(min(up,down,left,right,front,back))

#set boudary temperature
for i in range(y):
    for j in range(z):
        T[0][i][j]=up
        T[x-1][i][j]=down
    
for i in range(x):
    for j in range(z):
        T[i][0][j]=left
        T[i][y-1][j]=right

for i in range(x):
    for j in range(y):
        T[i][j][0]=front
        T[i][j][z-1]=back

# Set the tick of contour and colorbar
TickLevel = np.arange(20,201,20)

#Start repeating procedure 
repeat=2000
for iteration in range(0, repeat):
    for i in range(1,x-1,1):
        for j in range(1,y-1,1):
            for k in range(1,z-1,1):
                T[i,j,k]=(1/6)*(T[i+1][j][k]+T[i-1][j][k]+T[i][j+1][k]+T[i][j-1][k]+T[i][j][k+1]+T[i][j][k-1]) 
                
#print final condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc='C:\\Users\\Ivan Chen\\final_project\\laplace_3d\\case1\\case1_z_'
'''
for i in range(0,z):
    SaveImage(T[i],TickLevel,'Final Temperature Distribution for z='+str(i),SaveLoc+str(i+1)+'.png')

