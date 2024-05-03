import numpy as np
import matplotlib.pyplot as plt

def gaussian(position):
    return (1/(np.sqrt(2*np.pi))) * np.exp((-1/2)*position**2)

if __name__ == '__main__':
    x_values = np.linspace(-4, 4, 1000)
    y_values = gaussian(x_values)

    plt.plot(x_values, y_values)
    plt.title('Gaussian Function')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.grid(True)
    plt.show()
