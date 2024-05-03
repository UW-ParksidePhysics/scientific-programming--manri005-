import numpy as np
import matplotlib.pyplot as plt

def wave_function(x, t, alpha, f, k, w):
    return np.exp(-(alpha*x - f*t)**2) * np.sin(k*x - w*t)

if __name__ == '__main__':
    t = 0
    alpha_values = [0.5, 1, 2]
    f = 3
    k = 3 * np.pi
    w = 3 * np.pi

    x_values = np.linspace(-4, 4, 1000)

    plt.figure(figsize=(10, 6))
    for alpha in alpha_values:
        y_values = wave_function(x_values, t, alpha, f, k, w)
        plt.plot(x_values, y_values, label=f'alpha = {alpha}')

    plt.title('Wave Function for Different Alpha Values')
    plt.xlabel('x')
    plt.ylabel('f(x, t)')
    plt.legend()
    plt.grid(True)
    plt.show()
