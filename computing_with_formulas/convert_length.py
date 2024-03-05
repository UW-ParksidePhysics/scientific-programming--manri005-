def convert_length(distance_in_km):

  
  # conversion factors
  inches_per_cm = 1 / 2.54
  feet_per_inch = 1 / 12
  yards_per_foot = 1 / 3
  mile_per_yard = 1 / 1760
  #conversion formulas
  distance_in_inches = distance_in_km * 100 * 1000 * inches_per_cm
  distance_in_feet = distance_in_inches * feet_per_inch
  distance_in_yards = distance_in_feet * yards_per_foot
  distance_in_miles = distance_in_yards * mile_per_yard
  
  print("Distance of current living place from campus:")
  print(f"Inches: {distance_in_inches}")
  print(f"Feet: {distance_in_feet}")
  print(f"Yards: {distance_in_yards}")
  print(f"Miles: {distance_in_miles}")
  return distance_in_inches, distance_in_feet, distance_in_yards, distance_in_miles
  
# define distance from campus in km 
distance_in_km = 20.44

distance_in_inches, distance_in_feet, distance_in_yards, distance_in_miles = convert_length(distance_in_km)


#Verification distance
verification_distance_km = 0.640
verification_distance_inches, verification_distance_feet,   verification_distance_yards, verification_distance_miles =   convert_length(verification_distance_km)

print(f"Verification for 0.640 kilometers:")
print(f"Inches: {verification_distance_inches}")
print(f"Feet: {verification_distance_feet}")
print(f"Yards: {verification_distance_yards}")
print(f"Miles: {verification_distance_miles}")