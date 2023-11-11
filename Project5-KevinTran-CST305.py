import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

stop='c'
while( stop != 's'):
    stop = input('Type C to enter r value or S to stop inputting:' )
    stop= stop.lower()
    if stop=='c':
        #take input for r
        k=float(input('Enter the value of r being used: '))
    else:
        break
    def lorenz(x, y, z, s=10, r=k, b=8/3):
        '''
        Given:
           x, y, z: a point of interest in three dimensional space
           s, r, b: parameters defining the lorenz attractor
        Returns:
           x_dot, y_dot, z_dot: values of the lorenz attractor's partial
               derivatives at the point x, y, z
        '''
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot


    dt = 0.01
    num_steps = 10000

# Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

# Set initial values
    xs[0], ys[0], zs[0] = (0.512, 0.256, 0.512)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

#Plot x
    plt.figure()
    plt.plot(xs, label = 'X')
    plt.title("Figure 1")
    plt.xlabel("t-Time")
    plt.ylabel("x - JPG")
    plt.legend()
    plt.grid(True)

#Plot y
    plt.figure()
    plt.plot(ys, label = 'Y')
    plt.title("Figure 2")
    plt.xlabel("t-Time")
    plt.ylabel("y - PNG")
    plt.legend()
    plt.grid(True)
    plt.show()

#Plot z
    plt.figure()
    plt.plot(zs, label = 'Z')
    plt.title("Figure 3")
    plt.xlabel("t-Time")
    plt.ylabel("z - GIF")
    plt.legend()
    plt.grid(True)

    plt.show()