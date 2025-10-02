import numpy as np
import matplotlib.pyplot as plt

X_POS = 0
Y_POS = 1
Z_POS = 2

N = 10
T = 300
k = 1.0


# basically saying that everyone is connected to everyone except itselff-z
# but never connected to itself: GRAPH!
A = np.ones((N,N)) - np.eye(N)  

# constructing unit-circle desired angle -> coordination
R = 5
theta = 2*np.pi*np.arange(N)/N
p_star = np.c_[R*np.cos(theta), R*np.sin(theta)]

# desired distances (locally)
D = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        if A[i,j]:
            D[i,j] = np.linalg.norm(p_star[i] - p_star[j])

dt = 0.02
print("Selected dt: {:.3f}".format(dt))

# weighted protocols 
def weight(d, distance = 0.5, delta = 1.5, eps=1e-3):
    return (1 - distance/d) / ((delta - d)**3)

# turns out all we need is making size 2-D
x = np.random.uniform(-5,5,size=(N,2)) 

plot_size = 10
plt.ion() 
fig, ax = plt.subplots()
sc = ax.scatter(x[:,0], x[:,1], c='blue')
ax.set_xlim(-plot_size,plot_size)
ax.set_ylim(-plot_size,plot_size)
ax.set_aspect('equal')

for _ in range(T):
    dx = np.zeros_like(x)
    for i in range(N):
        for j in range(N):
            if i == j or A[i,j]==0: continue
            xij = x[i] - x[j]
            d = np.linalg.norm(x[i] - x[j])
            # w = weight(d)
            # dx[i] += -w * (x[i] - x[j])
            
            # screw weight function copying straight from matlab code
            w = (d**2 - D[i,j]**2)
            dx[i] += -k * w * xij

    vmax = 3
    
    n = np.linalg.norm(dx, axis=1, keepdims=True)
    dx = np.where(n > vmax, dx * (vmax / n), dx)
    
    x = x + dt * dx
    
    
    # update scatter plot data
    sc.set_offsets(x)    
    plt.draw()
    plt.pause(0.1)

plt.ioff()
plt.show()