import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


X_POS = 0
Y_POS = 1
Z_POS = 2

N = 50
T = 180

# copying the rate of 10 from matlab script...
# welp 10 deosnt' work, uhh, try 5?
# trying 0.2 -> works!
alpha = 0.0002

# basically saying that everyone is connected to everyone except itselff-z
# but never connected to itself: GRAPH!
A = np.ones((N,N)) - np.eye(N)  

# sum of each row --> number of neighbors for each node
D = np.diag(A.sum(axis=1))

# tried doing this manually but i got confused
# Thanks CharGPT
# diagonal entries -> degrees of node
# all other entires -> -1 if there is a connection
L = D - A

# turns out all we need is making size 3-D
x = np.random.uniform(-5,5,size=(N,3)) 
history_location = [x.copy()]


plt.ion() 
fig = plt.figure()
# one SINGLE subplot, in 3D
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x[:,0], x[:,1], x[:,2], c='blue')

ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
ax.set_zlim(-6,6)

# apparently uhh, the aspect doesn't work anymore
ax.set_box_aspect([1,1,1])

for _ in range(T):
    x = x - alpha * (L @ x)
    history_location.append(x.copy())
    
    # update scatter data
    sc._offsets3d = (x[:,0], x[:,1], x[:,2])
    fig.canvas.draw_idle()
    
    plt.pause(0.1)

print("Consensus value (avg):", np.mean(history_location[0], axis=0))
print("Starting positions:\n", history_location[0])
print("Final positions:\n", history_location[-1])

plt.ioff()
plt.show()