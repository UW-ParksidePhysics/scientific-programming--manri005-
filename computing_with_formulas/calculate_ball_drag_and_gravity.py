# Define constants
drag_coefficient = 0.2  # unitless
air_density = 1.225  # kg/m^3
cross_area = 0.11  # m^2 (cross-sectional area of a soccer ball)
ball_radius = 0.11 / 2  # m (radius of a soccer ball)
ball_mass = 0.43  # kg
gravitational_acceleration = 9.81  # m/s^2

# Define velocities for hard and soft kicks
hard_kick_velocity = 25  # m/s
soft_kick_velocity = 10  # m/s

# Define function to compute drag force
def compute_drag_force(velocity):
    drag_force = 0.5 * drag_coefficient * air_density * cross_area * velocity**2
    return drag_force

# Define function to compute gravity force
def compute_gravity_force():
    gravitational_force = ball_mass * gravitational_acceleration
    return gravitational_force

# Compute forces for hard kick
drag_force_hard_kick = compute_drag_force(hard_kick_velocity)
gravity_force_hard_kick = compute_gravity_force()
ratio_hard_kick = drag_force_hard_kick / gravity_force_hard_kick

# Compute forces for soft kick
drag_force_soft_kick = compute_drag_force(soft_kick_velocity)
gravity_force_soft_kick = compute_gravity_force()
ratio_soft_kick = drag_force_soft_kick / gravity_force_soft_kick

# Print results
print("Forces on the soccer ball for a hard kick:")
print(f"Velocity: {hard_kick_velocity} m/s")
print(f"Drag force: {drag_force_hard_kick:.1f} N")
print(f"Gravity force: {gravity_force_hard_kick:.1f} N")
print(f"Ratio of drag force to gravity force: {ratio_hard_kick:.2f}")

print("\nForces on the soccer ball for a soft kick:")
print(f"Velocity: {soft_kick_velocity} m/s")
print(f"Drag force: {drag_force_soft_kick:.1f} N")
print(f"Gravity force: {gravity_force_soft_kick:.1f} N")
print(f"Ratio of drag force to gravity force: {ratio_soft_kick:.2f}")