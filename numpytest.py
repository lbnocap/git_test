import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
array1 = np.array([1, 2, 3, 4, 5],dtype=np.int8)
array2=np.arange(1,50,2)
print(array2)
array3=np.linspace(1,100,50)
print(array3)
array4=np.random.randint(1,20,(4,4))
print(array1.itemsize,array4.itemsize,array2.nbytes)
print(array4[0,2])