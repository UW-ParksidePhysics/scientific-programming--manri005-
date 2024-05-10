"""
 This code creates a scatter plot and curve plot for the data and the fit polynomial 
 """

__author__ =  'Olivia Manring'

import numpy as np
import matplotlib.pyplot as plt
import curve_fit_array as curve_fit_array

def plot_data_with_fit(data_array, fit_curve, data_format="x", fit_format="--"):
    scatter_plot = plt.plot(data_array[0], data_array[1], data_format)
    curve_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format)
    return scatter_plot, curve_plot

if __name__ == "__main__":
    data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
    test_curve = [np.linspace(-2, 2), np.linspace(-2, 2) ** 2]
    plot_data_with_fit(data, test_curve)
    plt.show()
