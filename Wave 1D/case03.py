def SaveImage(Z,PlotTitle,SaveLoc):
    fig,ax=plt.subplots()
    plt.ylim(-1,1)
    plt.title(PlotTitle)
    plt.plot(X,Z)
    plt.show()
    fig.savefig(SaveLoc)

#Case3 products of sin waves string
import numpy as np
import matplotlib.pyplot as plt
x=100.01
t=10
c=1 #coefficient of PDE

#setting boundary 
X=np.arange(0, x, 0.1)
T=[np.sin(X*np.pi)*np.sin(X*np.pi/10)]

#setting coefficients
h=x/100 #n
k=t/100 #m
L=c*k/h

#print initial condition
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc='C:\\Users\\Ivan Chen\\final_project\\wave_1d\\case03\\case03_'
'''
SaveImage(T[0],'Initial Condition',SaveLoc+'initial.png')

#Setting repeating procedure
P=[T[0]]
T+=[P[0]]

#Start repeating procedure 
for j in range(1,200):
    P=[]
    for i in range(1,len(X)-1):
        P+=[(L**2)*(T[j][i+1]+T[j][i-1])+2*(1-L**2)*(T[j][i])-T[j-1][i]]
    P=([T[j][0]]+P)
    P+=[T[j][-1]]
    T+=[P]
    
#print final result of the wave    
'''
    #Please select where you would like to save your file
    #For example:
SaveLoc02='C:\\Users\\Ivan Chen\\final_project\\wave_1d\\case03\\case03_'
'''
for i in range(len(T)):
    SaveImage(T[i],'Case03 t='+str(round(k*i,2)),SaveLoc02+'t='+str(round(k*i,2))+'.png')
