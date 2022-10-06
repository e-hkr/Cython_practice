import numpy as np


def read_binary_py(num_days, skip=0):
  for i in range(num_days):
    np.fromfile('./sample.dat', dtype='>f', count=4500*24, offset=4500*24*(i+skip))\
      .reshape(24,5,30,30)
