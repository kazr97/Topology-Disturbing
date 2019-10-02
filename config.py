import numpy as np
import math

class curve:
    def __init__(self,X,Y,Z):
        self.X=X
        self.Y=Y
        self.Z=Z

#combine 2 curve into 1 curve
def intersection(curve1,curve2,theta=45,delta=0.0001):
    X=[]
    Y=[]
    Z=[]
    v1=-math.tan(theta)
    v2=math.tan(theta)
    for i in range(len(curve1.X)):
        sub_list=[]
        y_list=[]
        z_list=[]
        for j in range(int((curve2.Y[i]/2-curve1.Y[i]/2)/delta)):
            y=curve1.Y[i]/2+ j * delta
            z1=v1*(y-curve1.Y[i])+curve1.Z[i]
            z2=v2*(y-curve2.Y[i])+curve2.Z[i]
            sub_list.append(abs(z1-z2))
            y_list.append(y)
            z_list.append(z1)

        #print(sub_list)
        index=sub_list.index(min(sub_list))
        X.append(curve1.X[i])
        Y.append(y_list[index])
        Z.append(z_list[index])
    

    X=np.array(X)
    Y=np.array(Y)
    Z=np.array(Z)
    return curve(X,Y,Z)

#extend the curve down to the floor
def extend(surface_Z,curve):
    for j in range(len(surface_Z[0])):
        for i in range(len(surface_Z)):
            #print(surface_Z[i][j],curve3.Z[j])
            if (surface_Z[i][j]>curve.Z[j]):
               surface_Z[i][j]=curve.Z[j]
