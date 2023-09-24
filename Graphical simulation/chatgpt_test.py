import matplotlib.pyplot as plt
import numpy as np

def pisano_sequence(n):
    pisano_seq = [0, 1]
    a, b = 0, 1
    while True:
        a, b = b, (a + b) % n
        if (a, b) == (0, 1):
            break
        pisano_seq.append(b)
    return pisano_seq

def plot_pisano_sequence_on_circle(radius, n):
    pisano_seq = pisano_sequence(n)
    theta = np.linspace(0, 2 * np.pi, len(pisano_seq), endpoint=False)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'bo', label='Pisano Sequence')
    ax.plot(x[-1], y[-1], 'ro', label='Starting Point')

    for i in range(len(pisano_seq)):
        if i < len(pisano_seq) - 1:
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], 'b-')

    # Set the aspect ratio to be equal to ensure a perfect circle
    ax.set_aspect('equal', adjustable='box')

    # Label the axes and add a legend
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()

    # Display the plot
    plt.grid(True)
    plt.title(f'Pisano Sequence of {n} on Circle with Radius {radius}')
    plt.show()

# Call the function with the desired radius (in this case, 5) and n (Pisano sequence modulo)
radius = 5
n = 3
plot_pisano_sequence_on_circle(radius, n)
