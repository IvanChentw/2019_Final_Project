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

#Case5  A circular heater bounded by a circle space. 
import matplotlib.pyplot as plt
import numpy as np

#range of x and y and z:
x=30
y=30
z=30
R=(z-1)/2

#check whether between center<(x,y,z)<R
def circle_with_center(x,y,z,center): 
    if (x-R)**2+(y-R)**2+(z-R)**2<R**2 and (x-R)**2+(y-R)**2+(z-R)**2>center**2:
        return True
    else:
        return False

#boundary temperature
inside=200
outside=20


#create initialize points in x,y,z for T
T = np.empty((x,y,z))
T.fill(outside)
X = np.arange(0, x, 1)
Y = np.arange(0, y, 1)
Z = np.arange(0 ,z, 1)
T = np.empty((x,y,z))
T.fill(outside)

#set boundary and inside temperature

if (z-1)%2==0:
    T[(z-1)//2][(z-1)//2][(z-1)//2]=inside
    
for i in range(0,x,1):
    for j in range(0,y,1):
        for k in range(0,z,1):
            if circle_with_center(i,j,k,0):
                T[i][j][k]=inside  

#Start repeating procedure 
repeat=2000

for iteration in range(0, repeat):
    for i in range(1,x-1,1):
        for j in range(1,y-1,1):
            for k in range(1,z-1,1):
                if circle_with_center(i,j,k,3):
                    T[i,j,k]=(1/6)*(T[i+1][j][k]+T[i-1][j][k]+T[i][j+1][k]+T[i][j-1][k]+T[i][j][k+1]+T[i][j][k-1])   

#print final condition temperature
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc='C:\\Users\\Ivan Chen\\final_project\\laplace_3d\\case5\\case5_z_'
'''
for i in range(0,z):
    SaveImage(T[i],TickLevel,'Final Temperature Distribution for z='+str(i),SaveLoc+str(i+1)+'.png')
