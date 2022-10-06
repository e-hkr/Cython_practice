import numpy as np

def read_binary_py(skip=0):
  data = np.fromfile('./sample.dat', dtype='>f', count=4500*24, offset=4500*24*skip)\
           .reshape(24,5,30,30)
  return data[0,0]
