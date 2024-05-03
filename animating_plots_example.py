import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation


def temperature(depth, time, parameters):

  return parameters[0] + \
  parameters[1] * np.exp(-parameters[2] * depth) * \
  np.cos(parameters[3]*time - parameters[2]*depth)


def update_figure(frame)

plot_curve.set_ydata(temperature[frame])

if __name__ == '__main__':
  matplotlib.use('TkAgg')

thermal_diffusivity = 1.e-6
  oscillation_period = 24 * 60 * 60
  number_of_oscillations = 50

  mean_surface_temperature = 10
  temperature_amplotude = 10
  depth_sample_number =501

  number_of_animations_frams = 40
  frame_delay_time = 60

  angular_frequency = 2*np.pu / oscillation_period
  time_step = oscillation_period / 24
  maximum_time = number_of)oscillations*oscillation