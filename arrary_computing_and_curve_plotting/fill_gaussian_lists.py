import numpy as np

def gaussian(position):
    return (1/(np.sqrt(2*np.pi))) * np.exp((-1/2)*position**2)

if __name__ == '__main__':
    positions = np.linspace(-4, 4, 41)
    gaussian_values = [gaussian(pos) for pos in positions]

    print("Positions:", positions)
    print("Gaussian Values:", gaussian_values)
