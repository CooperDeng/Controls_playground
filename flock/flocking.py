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

# figuring out the alpha value we should be looking at
eigvals = np.linalg.eigvals(L)
lambda_max = max(eigvals.real)
print("λ_max =", lambda_max)
print("Stable alpha region: (0, {:.3f})".format(2/lambda_max))

alpha = 0.9 * (2/lambda_max)
dt = 0.09

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

# randomly generate the "agreed upon" flocking angle
# haven't figured out how exactly v0 works now
v0 = 1
phi = np.random.uniform(-np.pi, np.pi, size=N)
for _ in range(T):
    
    phi = phi - alpha * (L @ phi)
    phi = np.arctan2(np.sin(phi), np.cos(phi))
    v = np.column_stack((np.cos(phi), np.sin(phi))) * v0 
    x = x + dt * v
    
    history_location.append(x.copy())
    
    # update scatter plot data
    sc.set_offsets(x)    
    fig.canvas.draw_idle()    
    plt.pause(0.1)

plt.ioff()
plt.show()