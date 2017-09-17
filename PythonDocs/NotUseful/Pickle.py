from scipy import *
import pickle
mymat=zeros((10,10),dtype=float)
print mymat


import pickle
f=open('mymatrix.pickle','r')
foo=pickle.load(f)
print foo