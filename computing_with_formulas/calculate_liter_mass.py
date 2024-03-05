def calculate_mass(density_in_grams_per_cm3):
  # Volume of one liter in cm^3
  volume_cm3 = 1000

  # Calculate mass using density = mass / volume
  mass_in_grams = density_in_grams_per_cm3 * volume_cm3

  return mass_in_grams

# Density values in g/cm^3
density_values = {
  "Iron": 7.87,
  "Air": 0.001225,
  "Gasoline": 0.755,
  "Ice": 0.9167,
  "Human body": 1.06,
  "Silver": 10.49,
  "Platinum": 21.45
}

# Calculate and print the mass of one liter for each substance
for substance, density in density_values.items():
  mass_in_grams = calculate_mass(density)
  print(f"Mass of one liter of {substance}: {mass_in_grams:} grams")
 
