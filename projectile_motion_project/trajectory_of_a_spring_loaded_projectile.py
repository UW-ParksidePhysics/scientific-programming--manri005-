# This code simulates the projectile motion of an object launched by a spring 
# mechanism at various angles. It begins by defining the initial velocity of the 
# projectile based on the properties of the spring system. Using this velocity and 
# gravitational acceleration, the code calculates the trajectory of the projectile 
# for different launch angles. The trajectory is determined by calculating the 
# height of the projectile at various horizontal distances using the kinematic 
# equations of motion. Finally, the code generates a plot showing the trajectories 
# of the projectile for each launch angle, providing a visual representation
# how the angle affects the range and height of the projectile.

import numpy as np
import matplotlib.pyplot as plt

def initial_velocity(spring_constant, mass, spring_displacement):
    """
    Calculate initial velocity of the projectile.

    Args:
        spring_constant (float): Spring constant in N/m.
        mass (float): Mass of the object in kg.
        spring_displacement (float): Displacement of the spring in meters.

    Returns:
        float: Initial velocity of the projectile in m/s.
    """
    return np.sqrt(spring_constant * spring_displacement / mass)

def calculate_height(x, theta, initial_velocity):
    """
    Calculate height of the projectile at a given horizontal distance.

    Args:
        x (numpy.ndarray): Array of horizontal distances in meters.
        theta (float): Launch angle in radians.
        initial_velocity (float): Initial velocity of the projectile in m/s.

    Returns:
        numpy.ndarray: Array of vertical heights corresponding to the given horizontal distances.
    """
    return (np.tan(theta) * x - 
            (9.81 * x**2) / 
            (2 * (initial_velocity**2) * np.cos(theta)**2))

def maximum_distance(initial_velocity_values, theta, gravitational_acceleration): 
    """
    Calculate the maximum horizontal distance of the projectile.

    Args:
        initial_velocity_values (float): Initial velocity of the projectile in m/s.
        theta (float): Launch angle in radians.
        gravitational_acceleration (float): Acceleration due to gravity in m/s^2.

    Returns:
        float: Maximum horizontal distance of the projectile in meters.
    """
    return (initial_velocity_values**2 * np.sin(2 * theta)) / gravitational_acceleration

def x_values(maximum_distance):
    """
    Generate an array of x-values for plotting.

    Args:
        maximum_distance (float): Maximum horizontal distance of the projectile in meters.

    Returns:
        numpy.ndarray: Array of x-values.
    """
    return np.linspace(0, maximum_distance * 1.7, 100)

def calculate_projectile_motion(spring_constant, mass, spring_displacement, theta_degrees):
    """
    Calculate and plot the projectile motion.

    Args:
        spring_constant (float): Spring constant in N/m.
        mass (float): Mass of the object in kg.
        spring_displacement (float): Displacement of the spring in meters.
        theta_degrees (list): List of launch angles in degrees.
    """
    gravitational_acceleration = 9.81  # acceleration due to gravity (m/s^2)
    theta_radians = np.deg2rad(theta_degrees)

    plt.figure(figsize=(8, 6))  # Set figure size
    for theta_rad in theta_radians:
        initial_velocity_values = initial_velocity(spring_constant, mass, spring_displacement)
        max_dist = maximum_distance(initial_velocity_values, theta_rad, gravitational_acceleration)
        y_values = calculate_height(x_values(max_dist), theta_rad, initial_velocity_values)
        plt.plot(x_values(max_dist), y_values, label=f'{round(np.rad2deg(theta_rad))}°')

    plt.title('Trajectories of a Mass')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.ylim(0, max(y_values) * 1.2)  # Set y-axis limits from 0 to maximum y-value
    plt.legend(title='Launch Angle')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    spring_constant = 3  # N/m
    mass = 8  # kg
    spring_displacement = 20 / 1000  # convert mm to m
    theta_degrees = [30, 45, 60, 70]
    calculate_projectile_motion(spring_constant, mass, spring_displacement, theta_degrees)
