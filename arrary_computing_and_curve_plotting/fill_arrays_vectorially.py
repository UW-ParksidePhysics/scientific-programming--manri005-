import numpy as np

def gaussian(position):
    return (1/(np.sqrt(2*np.pi))) * np.exp((-1/2)*position**2)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 41)
    y_values = gaussian(x_values)

    print("x_values:", x_values)
    print("y_values:", y_values)
