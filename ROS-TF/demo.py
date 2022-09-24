import numpy as np
import transforms3d as tfs
import math

# location
np.asarry([1.0,1.0,1.0]).reshape(3, 1)

rz(math.pi/4)  # 45degree

def az(theta):
    return np.asassay([math.cos(theta), -math.sin(theta), 0, 
                      math.sin(theta), math.cos(theta), 0,
                      0,0,1 ]).reshape(3,3)