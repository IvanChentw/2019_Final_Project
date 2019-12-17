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

#Case4  A square heater bounded by a square space.
import matplotlib.pyplot as plt
import numpy as np

#range of x and y and z:
x=50
y=50
z=50
R=(z-1)/2

#check whether between center<(x,y,z)<R
def center(x,y,z,center):
    if abs(x-R)<=center and abs(y-R)<=center and abs(z-R)<=center:
        return True
    else:
        return False

#set boundary and inside temperature
inside=200
outside=20

#create initialize points in x,y,z for T
X = np.arange(0, x, 1)
Y = np.arange(0, y, 1)
Z = np.arange(0 ,z, 1)
T = np.empty((x,y,z))
T.fill(outside)

#set boundary and inside temperature

for i in range(0,x,1):
    for j in range(0,y,1):
        for k in range(0,z,1):
            if center(i,j,k,R-1):
                T[i][j][k]=inside

#Start repeating procedure
repeat=2000

for iteration in range(0, repeat):
    for i in range(1,x-1,1):
        for j in range(1,y-1,1):
            for k in range(1,z-1,1):
                if not center(i,j,k,3):
                    T[i,j,k]=(1/6)*(T[i+1][j][k]+T[i-1][j][k]+T[i][j+1][k]+T[i][j-1][k]+T[i][j][k+1]+T[i][j][k-1])

#print final condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc='C:\\Users\\Ivan Chen\\final_project\\laplace_3d\\case4\\case4_z_'
'''
for i in range(0,z):
    SaveImage(T[i],TickLevel,'Final Temperature Distribution for z='+str(i),SaveLoc+str(i+1)+'.png')

