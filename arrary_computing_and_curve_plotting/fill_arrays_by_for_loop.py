import numpy as np

def gaussian(position):
    return (1/(np.sqrt(2*np.pi))) * np.exp((-1/2)*position**2)

if __name__ == '__main__':
    positions = np.linspace(-4, 4, 41)

    x_values = np.empty_like(positions)
    y_values = np.empty_like(positions)

    for i, pos in enumerate(positions):
        x_values[i] = pos
        y_values[i] = gaussian(pos)

    print("x_values:", x_values)
    print("y_values:", y_values)
