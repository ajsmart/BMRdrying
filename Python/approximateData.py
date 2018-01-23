import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The object of this code is to use linear regression to model the measurement
# data that has been collected.  This is to be used to model the drying
# electrode mathematically as a function of time

if __name__ == '__main__':
    #import the relevant data.
    pdata = pd.read_csv('data/Laser/01.16.18_031_laser_open.csv')
    sdata = pdata['-999.999'].as_matrix()
    num = 6 # number of legandre polynomials we will use to model data
    len = sdata.size

    # generate legandre polynomials through orthogonalization
    t = np.linspace(0,len,len)
    s = (len, num)
    p = np.zeros(s)
    for i in range(0,num):
        p[:,i] = t**i
    # now to orthogonalize those polynomials
    e = p
    q = np.zeros(s)
    np1 = np.linalg.norm(p[:,0])
    q[:,0] = p[:,0]/np1
    for j in range(1,num):
        for k in range(0,j):
            e[:,j] = e[:,j] - p[:,j].dot(q[:,k])/np.float(len)*q[:,k]
        nej = np.linalg.norm(e[:,j])
        q[:,j] = e[:,j]/nej
    
    #plt.figure(1)
    #plt.plot(t,q)
    #plt.title('Legendre Polynomials')
    #plt.show()
    
    # now lets get the approximation
    a = np.zeros([num,1])  #a is for Legandre approximation
    for i in range(0,num):
        a[i] =sdata.dot(q[:,i]) / np.float(len)

    g = np.zeros([num,num])
    for i in range(0,num):
        for j in range(0,num):
            g[i,j] = q[:,i].dot(q[:,j])/np.float(len)

    c = (g**-1).dot(a)
    plt.figure(2)
    plt.plot(t,sdata,'b',t,(c.conj().T.dot(q.conj().T)).conj().T,'r')
    plt.title('Legandre Approximation')
    plt.show()
