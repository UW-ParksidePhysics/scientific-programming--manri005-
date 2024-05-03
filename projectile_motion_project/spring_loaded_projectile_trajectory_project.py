import numpy as np
import matplotlib.pyplot as plt

# Define initial velocity
spring_constant = 3  # N/m
mass = 8  # kg
spring_displacement = 20 /1000  # convert mm to m

def initial_velocity(spring_constant, mass, spring_displacement):
    return np.sqrt(spring_constant * spring_displacement / mass)  # m/s

# Constants
gravitational_acceleration = 9.81  # acceleration due to gravity (m/s^2)

# Define a list of launch angles in degrees
theta_degrees = [30, 45, 60, 70]

# Convert angles to radians
theta_radians = np.deg2rad(theta_degrees)

# Function to calculate height as a function of x
def calculate_height(x, theta, initial_velocity):
    return (np.tan(theta) * x - 
            (gravitational_acceleration * x**2) / 
            (2 * (initial_velocity**2) * np.cos(theta)**2))

# Calculate maximum horizontal distance for the largest angle
# Calculate maximum horizontal distance for the given launch angle
def maximum_distance(initial_velocity_values, theta, gravitational_acceleration): 
    return (initial_velocity_values**2 * np.sin(2*theta)) / gravitational_acceleration


# Set the range of x-values
def x_values(maximum_distance):
    return np.linspace(0, maximum_distance * 1.7, 100)  # adjust the multiplier as needed for visibility

if __name__ == "__main__":

  # Plotting
  plt.figure(figsize=(8, 6))  # Set figure size
  for theta_rad in theta_radians:
    initial_velocity_values = initial_velocity(spring_constant, mass, spring_displacement)
    max_dist = maximum_distance(initial_velocity_values, theta_rad, gravitational_acceleration)  # Use theta_rad here
    y_values = calculate_height(x_values(max_dist), theta_rad, initial_velocity_values)
    plt.plot(x_values(max_dist), y_values, label=f'{round(np.rad2deg(theta_rad))}°')


  plt.title('Trajectories of a Mass')
  plt.xlabel('Horizontal Distance (m)')
  plt.ylabel('Vertical Distance (m)')
  plt.ylim(0, max(y_values) * 1.2)  # Set y-axis limits from 0 to maximum y-value
  plt.legend(title='Launch Angle')
  plt.grid(True)
  plt.show()


