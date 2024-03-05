# Define constants
mass_small = 45  # g
mass_large = 67  # g
density = 1.038  # g/cm^3
specific_heat_capacity = 3.7  # J/g°C
thermal_conductivity = 5.4e-3  # W/cm°C
boiling_water_temperature = 100  # °C

# Define function to compute cook time
def compute_cook_time(mass, initial_temperature, water_temperature):
    delta_T = water_temperature - initial_temperature
    k = thermal_conductivity / (density * specific_heat_capacity)
    time = (mass**(2/3) * specific_heat_capacity * delta_T) / (k * 0.76**(1/3))
    return time

# Compute cook times for large and small eggs from fridge
cook_time_large_fridge = compute_cook_time(mass_large, 4, boiling_water_temperature)
cook_time_small_fridge = compute_cook_time(mass_small, 4, boiling_water_temperature)

# Compute cook times for large and small eggs from room temperature
cook_time_large_room_temp = compute_cook_time(mass_large, 20, boiling_water_temperature)
cook_time_small_room_temp = compute_cook_time(mass_small, 20, boiling_water_temperature)

# Print results
print("Cook times for eggs from the fridge:")
print(f"Large egg: {cook_time_large_fridge:.0f} s = {cook_time_large_fridge / 60:.1f} min")
print(f"Small egg: {cook_time_small_fridge:.0f} s = {cook_time_small_fridge / 60:.1f} min")

print("\nCook times for eggs from room temperature:")
print(f"Large egg: {cook_time_large_room_temp:.0f} s = {cook_time_large_room_temp / 60:.1f} min")
print(f"Small egg: {cook_time_small_room_temp:.0f} s = {cook_time_small_room_temp / 60:.1f} min")