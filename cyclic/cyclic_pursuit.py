import numpy as np
import matplotlib.pyplot as plt

X_POS = 0
Y_POS = 1
Z_POS = 2

N = 20
T = 300

# basically saying that everyone is connected to everyone except itselff-z
# but never connected to itself: GRAPH!
A = np.ones((N,N)) - np.eye(N)  
# sum of each row --> number of neighbors for each node
D = np.diag(A.sum(axis=1))
# diagonal entries -> degrees of node
# all other entires -> -1 if there is a connection
L = D - A

'''
# figuring out the alpha value we should be looking at
eigvals = np.linalg.eigvals(L)
lambda_max = max(eigvals.real)
print("λ_max =", lambda_max)
print("Stable alpha region: (0, {:.3f})".format(2/lambda_max))
'''

dt = 0.2
print("Selected dt: {:.3f}".format(dt))

psi = np.pi / N

# rotation matrix - 2D
# 3D rotation matrix needs to specify the axis of rotation too
def R(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta),  np.cos(theta)]])

# ... a perfect circular motion is asymptotically achieved – so-called cyclic pursuit
Rpsi = R(-psi)

# turns out all we need is making size 2-D
x = np.random.uniform(-5,5,size=(N,2)) 
history_location = [x.copy()]

plot_size = 10

plt.ion() 
fig, ax = plt.subplots()
sc = ax.scatter(x[:,0], x[:,1], c='blue')
ax.set_xlim(-plot_size,plot_size)
ax.set_ylim(-plot_size,plot_size)
ax.set_aspect('equal')

for _ in range(T):
    v = np.zeros_like(x)
    for i in range(N):
        j = (i + 1) % N
        v[i] = Rpsi @ (x[j] - x[i])   # cyclic pursuit dynamics

    x = x + dt * v
    
    history_location.append(x.copy())
    
    # update scatter plot data
    sc.set_offsets(x)    
    plt.draw
    plt.pause(0.1)

plt.ioff()
plt.show()