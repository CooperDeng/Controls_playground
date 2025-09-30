import numpy as np

N = 5
T = 60

# copying the rate of 10 from matlab script...
# welp 10 deosnt' work, uhh, try 5?
# trying 0.2 -> works!
alpha = 0.2                

# basically saying that everyone is connected to everyone else
# but never connected to itself: GRAPH!
A = np.ones((N,N)) - np.eye(N)  

# sum of each row --> number of neighbors for each node
D = np.diag(A.sum(axis=1))

# tried doing this manually but i got confused
# Thanks CharGPT
# diagonal entries -> degrees of node
# all other entires -> -1 if there is a connection
L = D - A

x = np.random.uniform(-5,5,size=N)  # initial 1D positions
history_location = [x.copy()]

for _ in range(T):
    x = x - alpha * (L @ x)
    history_location.append(x.copy())

print("Consensus value (avg):", np.mean(history_location[0]))

print("Starting position:", history_location[0])

print("Final positions:", history_location[-1])