import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def homogeneous_matrix(rotation_matrix,vector):
    hom_matrix=np.zeros((4,4))
    hom_matrix[0:3,0:3]=rotation_matrix
    hom_matrix[0:3, 3]=vector
    hom_matrix[3,3]=1
    return hom_matrix
def rot_z(angle):
    """
    z ekseni etrafında dönme matrisi 
    angle:dönme açısı derece cinsinden
    return:3x3 numpy array
    """
    angle_rad=math.radians(angle)
    cosx=math.cos(angle_rad)
    sinx=math.sin(angle_rad)
    rotation_z=np.array([[cosx,-sinx,0],[sinx,cosx,0],[0,0,1]])
    return rotation_z
def hom_inverse(matrix):
    rotation_matrix=matrix[:3,:3]
    vector=matrix[:3, 3]
    r_transpose=np.transpose(rotation_matrix)
    new_vector=-(r_transpose@vector)
    hom_matrix=np.zeros((4,4))
    hom_matrix[:3,:3]=r_transpose
    hom_matrix[:3, 3]=new_vector
    hom_matrix[3,3]=1
    return hom_matrix
def plot_coordinate_system(ax,rotation_matrix,vector,system_name,scale=1.0):
    origin=vector.flatten()
    x_origin,y_origin,z_origin=origin[0],origin[1],origin[2]
    x=rotation_matrix[:, 0]*scale
    y=rotation_matrix[:, 1]*scale
    z=rotation_matrix[:, 2]*scale
    ax.quiver(x_origin, y_origin, z_origin, 
              x[0], x[1], x[2], 
              color='r', label=f'{system_name} X')
    ax.quiver(x_origin, y_origin, z_origin, 
              y[0],y[1], y[2], 
              color='g', label=f'{system_name} Y')
    ax.quiver(x_origin, y_origin, z_origin, 
              z[0],z[1],z[2], 
              color='b', label=f'{system_name} X')
    ax.scatter(x_origin,y_origin,z_origin,marker='o',color='k',s=20)
    ax.text(x_origin, y_origin, z_origin, f' {system_name} Orijin', color='k')
    

matrix=rot_z(90)
vector=np.array([5,2,8])
homogen_matrix=homogeneous_matrix(matrix,vector)
print(homogen_matrix)
inverse_matrix=hom_inverse(homogen_matrix)
print(inverse_matrix)
fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111,projection='3d')
plot_coordinate_system(ax,np.identity(3),np.array([0,0,0]),'Fixed Frame',scale=2)
r=homogen_matrix[:3,:3]
v=homogen_matrix[:3, 3]
plot_coordinate_system(ax, r, v, 'Mobile Frame', scale=2)
max_val = max(np.max(np.abs(v)) + 2, 3) 

ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('Z')
ax.legend()
plt.show()